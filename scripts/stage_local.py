"""Stage the exact ZIP in a disposable local marketplace. Does not install it."""

import argparse
import json
from pathlib import Path
import zipfile

from build import ROOT, build, read_json, review_gaps


def stage(destination):
    if destination.exists():
        raise ValueError("Choose a new staging directory; existing directories are never overwritten.")
    if review_gaps():
        raise ValueError("Resolve pending adaptation before host installation tests.")
    archive, _ = build(check=True)
    manifest = read_json(ROOT / "plugin.json")
    name = manifest["name"]
    display_name = manifest["extensions"]["com.openai"]["interface"]["displayName"]
    plugin = destination / "plugins" / name
    plugin.mkdir(parents=True)
    with zipfile.ZipFile(ROOT / archive) as package:
        package.extractall(plugin)
    catalog = destination / ".agents/plugins/marketplace.json"
    catalog.parent.mkdir(parents=True)
    catalog.write_text(json.dumps({
        "name": f"{name}-preview", "interface": {"displayName": f"{display_name} preview"},
        "plugins": [{"name": name, "source": {"source": "local", "path": f"./plugins/{name}"},
                     "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                     "category": "Developer Tools"}],
    }, indent=2) + "\n")
    print(destination.resolve())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    stage(parser.parse_args().destination)
