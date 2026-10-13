import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import publish_release as release

SHA = 'a' * 40
OTHER = 'b' * 40


class Forge:
    def __init__(self):
        self.head = SHA
        self.tag = None
        self.rows = []
        self.latest = None
        self.writes = []
        self.fail_upload = False
        self.advance_after_upload = False
        self.ref_type = 'commit'

    def __call__(self, method, path, body=None, **options):
        if method != 'GET':
            self.writes.append((method, path, copy.deepcopy(body)))
        if method == 'GET' and path == 'git/ref/heads/main':
            return {'object': {'sha': self.head}}
        if method == 'GET' and path == 'git/ref/tags/v0.1.2':
            return {'object': {'type': self.ref_type, 'sha': self.tag}} if self.tag else None
        if method == 'GET' and path.startswith('git/tags/'):
            return {'object': {'type': 'commit', 'sha': self.tag}}
        if method == 'GET' and path.startswith('releases?'):
            page = int(path.split('page=')[-1])
            return self.rows[(page - 1) * 100:page * 100]
        if method == 'POST' and path == 'git/refs':
            assert self.tag is None
            self.tag = body['sha']
            return {}
        if method == 'POST' and path == 'releases':
            row = dict(body, id=len(self.rows) + 1, assets=[], html_url='https://example.invalid/v0.1.2')
            self.rows.append(row)
            return row
        if method == 'POST' and '/assets?' in path:
            if self.fail_upload:
                self.fail_upload = False
                raise RuntimeError('interrupted upload')
            row = next(r for r in self.rows if r['id'] == int(path.split('/')[1]))
            asset = {'name': path.split('name=')[1], 'size': len(body), 'state': 'uploaded',
                     'digest': 'sha256:' + hashlib.sha256(body).hexdigest()}
            row['assets'].append(asset)
            if self.advance_after_upload:
                self.head = OTHER
            return asset
        if method == 'GET' and path == 'releases/latest':
            return next(r for r in self.rows if r['id'] == self.latest)
        if path.startswith('releases/'):
            row = next(r for r in self.rows if r['id'] == int(path.split('/')[1]))
            if method == 'PATCH':
                row.update(body)
                self.latest = row['id']
            return row
        raise AssertionError((method, path, body))


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.api = Forge()
        self.args = dict(sha=SHA, version='0.1.2', notes='## [0.1.2]\n\n- Exact version notes.',
                         assets={'pstack-0.1.2.zip': b'validated ZIP', 'pstack-0.1.2.zip.sha256': b'checksum'})

    def publish(self):
        return release.publish(self.api, **self.args)

    def test_publish_tag_notes_assets_and_latest_then_retry(self):
        self.assertIn('Published v0.1.2', self.publish())
        row = self.api.rows[0]
        self.assertEqual(self.api.tag, SHA)
        self.assertEqual(row['body'], self.args['notes'])
        self.assertFalse(row['draft'])
        self.assertFalse(row['prerelease'])
        self.assertEqual(self.api.latest, row['id'])
        self.assertEqual([a['name'] for a in row['assets']], list(self.args['assets']))
        self.publish()
        self.assertEqual(len(self.api.rows), 1)
        self.assertEqual(sum(method == 'POST' and path == 'git/refs' for method, path, _ in self.api.writes), 1)
        self.assertEqual(sum('/assets?' in path for _, path, _ in self.api.writes), 2)

    def test_failed_upload_recovers_draft_without_duplicate_tag_or_release(self):
        self.api.fail_upload = True
        with self.assertRaisesRegex(RuntimeError, 'interrupted'):
            self.publish()
        self.assertTrue(self.api.rows[0]['draft'])
        self.assertIsNone(self.api.latest)
        self.publish()
        self.assertEqual(len(self.api.rows), 1)
        self.assertFalse(self.api.rows[0]['draft'])

    def test_existing_asset_conflict_is_not_overwritten(self):
        self.publish()
        self.api.rows[0]['assets'][0]['digest'] = 'sha256:wrong'
        self.api.writes.clear()
        with self.assertRaisesRegex(ValueError, 'never overwritten'):
            self.publish()
        self.assertEqual(self.api.writes, [])

    def test_stale_run_and_version_cannot_downgrade_latest(self):
        self.api.head = OTHER
        self.assertIn('Skipped stale', self.publish())
        self.assertEqual(self.api.writes, [])
        self.api.head = SHA
        self.api.rows = [{'id': 9, 'tag_name': 'v0.2.0', 'draft': False, 'prerelease': False}]
        self.api.latest = 9
        self.assertIn('Skipped stale', self.publish())
        self.assertEqual(self.api.writes, [])
        self.assertEqual(self.api.latest, 9)

    def test_newer_release_on_later_page_is_respected(self):
        self.api.rows = [{'id': n, 'tag_name': f'v0.0.{n}', 'draft': False, 'prerelease': False} for n in range(100)]
        self.api.rows.append({'id': 100, 'tag_name': 'v1.0.0', 'draft': False, 'prerelease': False})
        self.assertIn('Skipped stale', self.publish())
        self.assertEqual(self.api.writes, [])

    def test_main_advance_after_staging_does_not_publish(self):
        self.api.advance_after_upload = True
        self.assertIn('Stopped stale', self.publish())
        self.assertTrue(self.api.rows[0]['draft'])
        self.assertIsNone(self.api.latest)
        self.assertFalse(any(method == 'PATCH' for method, _, _ in self.api.writes))

    def test_immutable_tag_at_other_commit_is_never_moved(self):
        self.api.tag = OTHER
        self.assertIn('Skipped immutable', self.publish())
        self.assertEqual(self.api.tag, OTHER)
        self.assertEqual(self.api.writes, [])

    def test_matching_annotated_tag_is_supported(self):
        self.api.tag = SHA
        self.api.ref_type = 'tag'
        self.publish()
        self.assertFalse(any(path == 'git/refs' for _, path, _ in self.api.writes))

    def test_notes_require_one_exact_nonempty_version(self):
        text = '# Changelog\n\n## [0.1.2] - today\n\n- Current.\n\n## [0.1.1]\n\n- Old.\n'
        self.assertEqual(release.release_notes(text, '0.1.2'), '## [0.1.2] - today\n\n- Current.')
        for value in ('# No version', '## [0.1.2]\n', '## [0.1.2]\n- One\n## [0.1.2]\n- Two'):
            with self.assertRaises(ValueError):
                release.release_notes(value, '0.1.2')

    def test_invalid_version_and_unqualified_context_do_not_publish(self):
        for version in ('0.1.2-rc.1', '01.2.3', 'latest', '1.2.3+meta'):
            with self.assertRaises(ValueError):
                release.version_tuple(version)
        for event, ref, result in [('pull_request', 'refs/heads/main', 'success'), ('push', 'refs/heads/topic', 'success'), ('push', 'refs/heads/main', 'failure')]:
            with patch.dict(os.environ, {'GITHUB_EVENT_NAME': event, 'GITHUB_REF': ref, 'VALIDATION_RESULT': result}):
                with self.assertRaisesRegex(ValueError, 'successful validation'):
                    release.main()

    def test_http_errors_fail_closed_except_explicit_missing_tag(self):
        import urllib.error
        api = release.GitHub('HellowLab/Pstack', 'test-token')
        for status in (403, 404, 500):
            error = urllib.error.HTTPError('https://api.github.com', status, 'fixture', {}, None)
            with patch.object(release.urllib.request, 'urlopen', side_effect=error):
                if status == 404:
                    self.assertIsNone(api('GET', 'git/ref/tags/v0.1.2', optional=True))
                else:
                    with self.assertRaises(RuntimeError):
                        api('GET', 'git/ref/tags/v0.1.2', optional=True)

    def test_workflow_gates_write_permission_on_main_validation(self):
        import yaml
        workflow = yaml.safe_load((release.ROOT / '.github/workflows/ci.yml').read_text())
        job = workflow['jobs']['release']
        self.assertEqual(job['needs'], 'validate')
        self.assertIn("github.ref == 'refs/heads/main'", job['if'])
        self.assertEqual(job['permissions'], {'contents': 'write'})
        self.assertEqual(job['concurrency'], {'group': 'pstack-github-release', 'cancel-in-progress': False})
        self.assertEqual(job['steps'][0]['with']['ref'], '${{ github.sha }}')


if __name__ == '__main__':
    unittest.main()
