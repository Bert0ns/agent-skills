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
| `using-agent-skills` | Session start, task routing, workflow selection | Meta-skill router that discovers and invokes the right skill across development phases. | `bertons-me` / `agent-skills` |

### Ideation, scoping, and context

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `idea-refine` | "ideate", "refine this idea", "stress-test my plan" | Clarifies concepts through structured divergent and convergent thinking. | `addyosmani/agent-skills` |
| `grill-me` | "grill me", "interview me", "stress-test my thinking" | Interviews the user to test assumptions before implementation starts. | `mattpocock/skills` |
| `grilling` | "grill", "grilling" | Core question engine used by grill-me. | `mattpocock/skills` |
| `context-engineering` | "context engineering", new sessions, task switching | Curates files, rules, and token budgets to prevent agent context degradation. | `addyosmani/agent-skills` |
| `caveman` | "/caveman", "caveman mode", "be brief", "less tokens" | Terse communication mode that strips conversational filler while preserving all technical facts. | `JuliusBrussee/caveman` |

### Code quality, review, and anti-slop

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `distributed-code-audit` | "codebase audit", "deep review", "full code quality inspection" | Partitions large repositories across parallel review agents and generates an HTML scorecard. | `bertons-me` |
| `code-review` | "review PR", "review since main", diff audits | Runs two parallel review passes for repo coding standards and task specifications. | `mattpocock/skills` |
| `code-simplification` | "simplify code", "reduce complexity", refactoring for clarity | Simplifies logic and reduces accidental abstraction while strictly preserving behavior. | `addyosmani/agent-skills` |
| `security-and-hardening` | "security review", "audit vulnerabilities", auth & input validation | Hardens code against OWASP Top 10 vulnerabilities, auth flaws, and dependency risks. | `addyosmani/agent-skills` |
| `thermo-nuclear-code-quality-review` | "thermonuclear review", deep code quality audit | Inspects code for bloated files, tangled conditionals, and leaky abstractions. | `cursor/plugins` |
| `deslop` | Post-generation cleanup, branch diffs | Removes AI boilerplate, excessive comments, and unnatural defensive checks from code. | `cursor/plugins` |
| `unslop` | Text review, documentation, prose edits | Removes AI filler words, sycophantic phrasing, and decorative patterns from prose. | `cursor/plugins` |

### Architecture and engineering practices

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `system-design-docs` | "system design", "document architecture", C4 blueprints, drift audit | Reverse-engineers and authors modular C4-aligned system design blueprints with verified Mermaid diagrams. | `bertons-me` |
| `tdd` | "tdd", "red-green-refactor", building new features | Guides test-driven development using red-green-refactor cycles. | `mattpocock/skills` |
| `improve-codebase-architecture` | "improve architecture", refactoring deep modules | Scans for shallow modules and produces an interactive HTML improvement report. | `mattpocock/skills` |
| `ponytail` | "ponytail", "be lazy", "simplest solution", "yagni" | Lazy senior dev mindset enforcing minimal diffs, YAGNI, and anti-overengineering. | `DietrichGebert/ponytail` |
| `typescript-best-practices` | Editing `.ts` or `.tsx` files | Applies rules for typed boundaries, runtime validation, and domain modeling. | `cursor/plugins` |

### Frontend, design systems, and mobile

| Skill | Triggers | Description | Source |
| :--- | :--- | :--- | :--- |
| `frontend-design` | "frontend design", designing UI, styling | Directs visual hierarchy, typography, and color palettes to avoid generic AI layouts. | `anthropics/skills` |
| `web-design-guidelines` | "review UI", "check accessibility", "audit design" | Audits interfaces against Web Interface Guidelines for accessibility, layout, and UX. | `vercel-labs/agent-skills` |
| `vercel-react-best-practices` | React/Next.js data fetching, performance tuning | Performance and composition rules for React and Next.js applications. | `vercel-labs/agent-skills` |
| `vercel-react-native-skills` | React Native, Expo, mobile app development | Performance patterns for React Native and Expo, with a focus on lists and animations. | `vercel-labs/agent-skills` |

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

1. Create a new skill directory:
   ```bash
   npx skills init <skill-name>
   ```
2. Move the directory into `skills/<skill-name>`.
3. Add instructions and examples in `skills/<skill-name>/SKILL.md`.
4. Add the skill name to the desired group in `skills.sh.json`.
5. Register the upstream repository or local origin in `skills.sources.json`.
6. Commit and push the changes.

---

## Automated weekly sync

A GitHub Actions workflow runs every Monday at 04:00 UTC (`.github/workflows/update-skills.yml`). The workflow reads upstream repository mappings from `skills.sources.json`, clones sources via `scripts/sync-upstream.py`, updates files in `skills/`, verifies discovery, and opens a pull request against `main` when changes are detected. Custom skills like `distributed-code-audit`, `system-design-docs`, and `using-agent-skills` are preserved.

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
