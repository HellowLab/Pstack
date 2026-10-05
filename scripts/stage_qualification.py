"""Create a disposable, synthetic Git fixture. Never invokes a model or a remote."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def stage(destination):
    source = ROOT / "tests/fixtures/qualification"
    destination.mkdir(parents=True)  # Refuse to overwrite an existing case.
    for path in sorted(source.iterdir()):
        if path.is_file():
            shutil.copyfile(path, destination / path.name)
    env = dict(os.environ)
    env.update({
        "GIT_AUTHOR_NAME": "Pstack fixture",
        "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
        "GIT_COMMITTER_NAME": "Pstack fixture",
        "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
        "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+00:00",
        "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+00:00",
    })

    def git(*args):
        return subprocess.check_output(
            ["git", "-C", str(destination), "-c", "core.hooksPath=/dev/null",
             "-c", "commit.gpgsign=false", *args], env=env, text=True).strip()

    git("init", "-q", "--initial-branch=main")
    git("add", ".")
    git("commit", "-qm", "fixture: initial in-memory delivery queue")
    queue = destination / "queue.py"
    queue.write_text(queue.read_text().replace("MAX_ATTEMPTS = 3", "MAX_ATTEMPTS = 2"))
    git("add", "queue.py")
    git("commit", "-qm", "fixture: limit delivery attempts to fit request deadline",
        "-m", "The adapter reserves 30 ms per attempt under an 80 ms total deadline. "
        "Allow at most two attempts; three can exceed that budget. "
        "This is a synthetic design rationale, not a recorded benchmark.")
    print(f"Fixture: {destination.resolve()}\nHEAD: {git('rev-parse', 'HEAD')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    stage(parser.parse_args().destination)
