#!/usr/bin/env python3
"""
Sync skills from upstream community repositories into the local skills/ directory.
Sources and upstream mappings are loaded from skills.sources.json.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile


def load_sources(sources_path):
    with open(sources_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("skills", {})


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sources_path = os.path.join(repo_root, "skills.sources.json")
    skills_dir = os.path.join(repo_root, "skills")
    os.makedirs(skills_dir, exist_ok=True)

    if not os.path.exists(sources_path):
        print(f"Error: {sources_path} not found.", file=sys.stderr)
        sys.exit(1)

    sources = load_sources(sources_path)

    # Filter skills configured for upstream sync
    sync_targets = {
        name: config
        for name, config in sources.items()
        if config.get("sync", False) and config.get("repository") != "local"
    }

    # Group target skills by upstream repository to clone each repo only once
    repos = {}
    for skill_name, config in sync_targets.items():
        repo_url = config["repository"]
        if not repo_url.endswith(".git"):
            repo_url = f"{repo_url}.git"
        rel_path = config["path"]
        repos.setdefault(repo_url, []).append((skill_name, rel_path))

    tmp_dir = tempfile.mkdtemp(prefix="skills-sync-")
    print(f"Syncing upstream skills via temporary workspace: {tmp_dir}")

    try:
        for idx, (repo_url, skill_list) in enumerate(repos.items(), start=1):
            clone_dest = os.path.join(tmp_dir, f"repo_{idx}")
            print(f"Cloning {repo_url} (depth 1)...")
            subprocess.run(
                ["git", "clone", "--depth", "1", repo_url, clone_dest],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            for skill_name, rel_path in skill_list:
                src_skill_path = os.path.join(clone_dest, rel_path)
                dest_skill_path = os.path.join(skills_dir, skill_name)

                if not os.path.exists(src_skill_path):
                    print(
                        f"WARNING: Source path not found for {skill_name}: {src_skill_path}",
                        file=sys.stderr,
                    )
                    continue

                if os.path.exists(dest_skill_path):
                    shutil.rmtree(dest_skill_path)

                shutil.copytree(src_skill_path, dest_skill_path)
                print(f"Updated {skill_name} from {repo_url}")

        print("All upstream skills synced successfully.")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
