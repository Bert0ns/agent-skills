# Personal Agent Skills Collection

Curated collection of procedural capabilities and playbooks for AI coding agents (compatible with Antigravity, Claude Code, Cursor, Codex, Windsurf, and Gemini CLI), indexed on [skills.sh](https://skills.sh/).

## 🚀 Quick Install

### Install all skills globally (all projects & agents)
```bash
npx skills add <your-github-username>/skills -g
```

### Install into a specific project
```bash
npx skills add <your-github-username>/skills
```

### Install a specific skill
```bash
npx skills add <your-github-username>/skills --skill unslop -g
```

---

## 📦 Included Skills Catalog

### 💡 Ideation & Scoping
| Skill | Trigger / When to Use | Description | Source |
| :--- | :--- | :--- | :--- |
| **`idea-refine`** | "ideate", "refine this idea", "stress-test my plan" | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. | `addyosmani/agent-skills` |
| **`grill-me`** | "grill me", "interview me", "stress-test my thinking" | Relentless interview loop to stress-test an idea, plan, or system design before writing code. | `mattpocock/skills` |
| **`grilling`** | "grill", "grilling" | Core design-tree interrogation engine powering `grill-me`. | `mattpocock/skills` |

### 🧹 Code Quality, Review & Anti-Slop
| Skill | Trigger / When to Use | Description | Source |
| :--- | :--- | :--- | :--- |
| **`unslop`** | Text editing, docs, blog posts, AI writing review | Cuts AI tells, buzzwords, and boilerplate from written prose and documentation. | `cursor/plugins` |
| **`deslop`** | Post-generation code cleanup, branch diffs | Removes AI-generated code slop, overly verbose stubs, and restores clean idioms. | `cursor/plugins` |
| **`code-review`** | "review PR", "review since main", diff audits | Parallel two-axis review checking both adherence to repository coding standards and spec fulfillment. | `mattpocock/skills` |
| **`thermo-nuclear-code-quality-review`** | "thermonuclear review", deep code quality audit | Ultra-strict maintainability review flagging leaking abstractions, bloated files, and spaghetti conditions. | `cursor/plugins` |

### 🛠️ Architecture & Engineering Practices
| Skill | Trigger / When to Use | Description | Source |
| :--- | :--- | :--- | :--- |
| **`tdd`** | "tdd", "red-green-refactor", building new features | Strict test-driven development loop emphasizing behavior over implementation details. | `mattpocock/skills` |
| **`improve-codebase-architecture`** | "improve architecture", refactoring deep modules | Scans the codebase for deepening opportunities and presents a structured interactive report. | `mattpocock/skills` |
| **`typescript-best-practices`** | Editing `.ts` or `.tsx` files | Type-system discipline: illegal states unrepresentable, branded primitives, boundary validation. | `cursor/plugins` |

### ⚛️ React & Mobile Engineering
| Skill | Trigger / When to Use | Description | Source |
| :--- | :--- | :--- | :--- |
| **`vercel-react-best-practices`** | React/Next.js data fetching, performance tuning | Complete catalog of React and Next.js performance and composition rules from Vercel Engineering. | `vercel-labs/agent-skills` |
| **`vercel-react-native-skills`** | React Native, Expo, mobile app development | Mobile-specific best practices, list performance, native module integration, and reanimated tips. | `vercel-labs/agent-skills` |

---

## 🛠️ Repository Structure

```text
.
├── skills.sh.json                 # Directory grouping and display configuration for skills.sh
├── skills/
│   ├── code-review/
│   ├── deslop/
│   ├── grill-me/
│   ├── grilling/
│   ├── idea-refine/
│   ├── improve-codebase-architecture/
│   ├── tdd/
│   ├── thermo-nuclear-code-quality-review/
│   ├── typescript-best-practices/
│   ├── unslop/
│   ├── vercel-react-best-practices/
│   └── vercel-react-native-skills/
├── README.md
└── .gitignore
```

---

## ➕ Adding a New Skill

1. Initialize a new skill directory:
   ```bash
   npx skills init <skill-name>
   ```
2. Place the resulting folder inside `skills/<skill-name>`.
3. Add your procedural rules and guidelines into `skills/<skill-name>/SKILL.md`.
4. Register the new skill slug under the appropriate group in `skills.sh.json`.
5. Commit and push to GitHub.

---

## 🔄 Updating Installed Skills

To fetch updates across your machines:
```bash
npx skills update -g
```
