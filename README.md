# Agent skills

Skills for coding agents such as Antigravity, Claude Code, Cursor, Codex, Windsurf, and Gemini CLI, indexed on [skills.sh](https://skills.sh/).

## Quick install

### Install all skills globally

```bash
npx skills add Bert0ns/agent-skills -g
```

### Install into a project

```bash
npx skills add Bert0ns/agent-skills
```

### Install a specific skill

```bash
npx skills add Bert0ns/agent-skills --skill distributed-code-audit -g
```

---

## Included skills

### Meta, routing, and workflows

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `using-agent-skills` | Session start, task routing, workflow selection | Routes tasks to the matching skill across development phases. | `bertons-me` / `agent-skills` |

### Ideation, scoping, and context

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `idea-refine` | "ideate", "refine this idea", "stress-test my plan" | Clarifies concepts through structured divergent and convergent thinking. | `addyosmani/agent-skills` |
| `grill-me` | "grill me", "interview me", "stress-test my thinking" | Interviews user to test assumptions before building. | `mattpocock/skills` |
| `grilling` | "grill", "grilling" | Question engine backing `grill-me`. | `mattpocock/skills` |
| `context-engineering` | "context engineering", new sessions, task switching | Curates active files, rules, and token budgets to keep context within limits. | `addyosmani/agent-skills` |
| `caveman` | "/caveman", "caveman mode", "be brief", "less tokens" | Terse communication voice that cuts fluff and saves tokens while keeping technical facts. | `JuliusBrussee/caveman` |

### Code quality, review, and anti-slop

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `distributed-code-audit` | "codebase audit", "deep review", "full code quality inspection" | Partitions codebase across parallel review agents and generates an HTML scorecard. | `bertons-me` |
| `code-review` | "review PR", "review since main", diff audits | Runs two review passes for repository standards and task specs. | `mattpocock/skills` |
| `code-simplification` | "simplify code", "reduce complexity", refactoring for clarity | Simplifies logic and cuts unnecessary abstractions without breaking behavior. | `addyosmani/agent-skills` |
| `security-and-hardening` | "security review", "audit vulnerabilities", auth & input validation | Audits code against OWASP Top 10, auth flaws, and dependency risks. | `addyosmani/agent-skills` |
| `thermo-nuclear-code-quality-review` | "thermonuclear review", deep code quality audit | Audits code for bloated files, tangled logic, and leaky abstractions. | `cursor/plugins` |
| `deslop` | Post-generation cleanup, branch diffs | Removes AI boilerplate, duplicate comments, and defensive clutter from code. | `cursor/plugins` |
| `unslop` | Text review, documentation, prose edits | Cuts AI writing tells, filler phrases, and sycophantic phrasing from prose. | `cursor/plugins` |

### Architecture and engineering practices

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `system-design-docs` | "system design", "document architecture", C4 blueprints, drift audit | Extracts system architecture into C4 diagrams and markdown documents with subagents. | `bertons-me` |
| `tdd` | "tdd", "red-green-refactor", building new features | Guides test-driven development with red-green-refactor loops. | `mattpocock/skills` |
| `improve-codebase-architecture` | "improve architecture", refactoring deep modules | Scans shallow modules and generates an interactive HTML report. | `mattpocock/skills` |
| `ponytail` | "ponytail", "be lazy", "simplest solution", "yagni" | Smallest working change, minimal diffs, standard libraries, and no bloat. | `DietrichGebert/ponytail` |
| `typescript-best-practices` | Editing `.ts` or `.tsx` files | Enforces typed boundaries, runtime validation, and domain modeling. | `cursor/plugins` |

### Frontend, design systems, and mobile

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `frontend-design` | "frontend design", designing UI, styling | Directs visual hierarchy, typography, and color to avoid generic default styling. | `anthropics/skills` |
| `web-design-guidelines` | "review UI", "check accessibility", "audit design" | Audits interfaces for accessibility, keyboard navigation, and layout consistency. | `vercel-labs/agent-skills` |
| `vercel-react-best-practices` | React/Next.js data fetching, performance tuning | Performance and composition rules for React and Next.js applications. | `vercel-labs/agent-skills` |
| `vercel-react-native-skills` | React Native, Expo, mobile app development | Performance patterns for React Native and Expo lists and animations. | `vercel-labs/agent-skills` |

---

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       └── update-skills.yml
├── scripts/
│   └── sync-upstream.py
├── skills.sh.json
├── skills.sources.json
├── skills/
│   ├── caveman/
│   ├── code-review/
│   ├── code-simplification/
│   ├── context-engineering/
│   ├── deslop/
│   ├── distributed-code-audit/
│   ├── frontend-design/
│   ├── grill-me/
│   ├── grilling/
│   ├── idea-refine/
│   ├── improve-codebase-architecture/
│   ├── ponytail/
│   ├── security-and-hardening/
│   ├── system-design-docs/
│   ├── tdd/
│   ├── thermo-nuclear-code-quality-review/
│   ├── typescript-best-practices/
│   ├── unslop/
│   ├── using-agent-skills/
│   ├── vercel-react-best-practices/
│   ├── vercel-react-native-skills/
│   └── web-design-guidelines/
├── README.md
└── .gitignore
```

---

## Adding a skill

1. Create a skill directory:
   ```bash
   npx skills init <skill-name>
   ```
2. Move the directory into `skills/<skill-name>`.
3. Add instructions and examples in `skills/<skill-name>/SKILL.md`.
4. Add the skill name to `skills.sh.json`.
5. Register the upstream repository or local origin in `skills.sources.json`.
6. Commit and push the changes.

---

## Automated weekly sync

A GitHub Actions workflow at `.github/workflows/update-skills.yml` runs every Monday at 04:00 UTC. It reads mappings from `skills.sources.json`, syncs upstream repos with `scripts/sync-upstream.py`, updates `skills/`, and opens a pull request against `main`. Custom skills (`distributed-code-audit`, `system-design-docs`, `using-agent-skills`) remain untouched.

To trigger the sync manually:
```bash
gh workflow run update-skills.yml
```

---

## Updating installed skills

To update installed skills across all local agents:
```bash
npx skills update -g
```
