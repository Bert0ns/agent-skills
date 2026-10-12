#!/usr/bin/env python3
"""
Sync skills from upstream community repositories into the local skills/ directory.
Excludes custom/local skills like distributed-code-audit.
"""

import os
import shutil
import subprocess
import tempfile
import sys

# Mapping: skill_name -> (git_repo_url, relative_path_in_repo)
UPSTREAM_MAP = {
    # mattpocock/skills
    "code-review": ("https://github.com/mattpocock/skills.git", "skills/engineering/code-review"),
    "grill-me": ("https://github.com/mattpocock/skills.git", "skills/productivity/grill-me"),
    "grilling": ("https://github.com/mattpocock/skills.git", "skills/productivity/grilling"),
    "tdd": ("https://github.com/mattpocock/skills.git", "skills/engineering/tdd"),
    "improve-codebase-architecture": ("https://github.com/mattpocock/skills.git", "skills/engineering/improve-codebase-architecture"),

    # cursor/plugins
    "unslop": ("https://github.com/cursor/plugins.git", "pstack/skills/unslop"),
    "deslop": ("https://github.com/cursor/plugins.git", "cursor-team-kit/skills/deslop"),
    "thermo-nuclear-code-quality-review": ("https://github.com/cursor/plugins.git", "thermos/skills/thermo-nuclear-code-quality-review"),
    "typescript-best-practices": ("https://github.com/cursor/plugins.git", "pstack/skills/typescript-best-practices"),

    # addyosmani/agent-skills
    "idea-refine": ("https://github.com/addyosmani/agent-skills.git", "skills/idea-refine"),
    "context-engineering": ("https://github.com/addyosmani/agent-skills.git", "skills/context-engineering"),

    # vercel-labs/agent-skills
    "vercel-react-best-practices": ("https://github.com/vercel-labs/agent-skills.git", "skills/react-best-practices"),
    "vercel-react-native-skills": ("https://github.com/vercel-labs/agent-skills.git", "skills/react-native-skills"),
    "web-design-guidelines": ("https://github.com/vercel-labs/agent-skills.git", "skills/web-design-guidelines"),

    # anthropics/skills
    "frontend-design": ("https://github.com/anthropics/skills.git", "skills/frontend-design"),
}


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(repo_root, "skills")
    os.makedirs(skills_dir, exist_ok=True)

    # Group target skills by upstream repository to clone each repo only once
    repos = {}
    for skill_name, (repo_url, rel_path) in UPSTREAM_MAP.items():
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
                    print(f"WARNING: Source path not found for {skill_name}: {src_skill_path}", file=sys.stderr)
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
