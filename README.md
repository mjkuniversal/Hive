# Hive

103 Claude Code agent definitions organized into 21 specialized teams.

## Teams

| # | Team | Agents | Focus |
|---|------|--------|-------|
| 1 | [Ops](agents/ops/) | 5 | System diagnostics, Docker, networking, hardware |
| 2 | [Design](agents/design/) | 5 | UI/UX, CSS, branding, marketing content |
| 3 | [Full-Stack](agents/fullstack/) | 5 | Frontend, backend, APIs, data engineering |
| 4 | [Extensions](agents/extensions/) | 4 | Browser extension dev (Firefox/Chrome) |
| 5 | [DevOps](agents/devops/) | 4 | Docker deployment, cloud platforms, CI/CD |
| 6 | [Automation](agents/automation/) | 4 | CRM, Google Sheets, workflows, reports |
| 7 | [QA & Security](agents/qa-security/) | 4 | Testing, security auditing, performance |
| 8 | [Research](agents/research/) | 5 | Codebase, web, system, network research |
| 9 | [Compliance](agents/compliance/) | 5 | Regulatory, privacy, policy, accessibility |
| 10 | [Content](agents/content/) | 5 | Technical writing, knowledge management |
| 11 | [Finance](agents/finance/) | 5 | Cost analysis, pricing, ROI, business strategy |
| 12 | [Incident Response](agents/incident-response/) | 5 | Incident management, runbooks, postmortems |
| 13 | [AI & Prompt](agents/ai-prompt/) | 5 | Prompt engineering, AI features, agent architecture |
| 14 | [Migration](agents/migration/) | 5 | Framework, schema, and platform migrations |
| 15 | [UX Research](agents/ux-research/) | 5 | User research, analytics, usability testing |
| 16 | [Marketing](agents/marketing/) | 6 | SEO, social media, ads, lead gen, email/SMS |
| 17 | [Sales](agents/sales/) | 6 | Sales process, proposals, coaching, CRM pipeline |
| 18 | [Admin](agents/admin/) | 5 | Scheduling, email, documents, meetings |
| 19 | [Accounting](agents/accounting/) | 5 | Bookkeeping, commissions, payroll, taxes |
| 20 | [Media Production](agents/media-production/) | 5 | Video, graphics, presentations, infographics |
| 21 | [Contracting](agents/contracting/) | 5 | Agent contracting, credentialing, onboarding |

## Structure

Each team has a **lead** (opus model) that coordinates **specialists** (sonnet model).

```
agents/
├── ops/                  # System operations
├── design/               # Visual design
├── fullstack/            # Web development
├── extensions/           # Browser extensions
├── devops/               # Deployment & infrastructure
├── automation/           # Business process automation
├── qa-security/          # Testing & security
├── research/             # Multi-domain research
├── compliance/           # Legal & regulatory
├── content/              # Writing & knowledge
├── finance/              # Financial analysis
├── incident-response/    # Reliability & incidents
├── ai-prompt/            # AI tooling optimization
├── migration/            # System migrations
├── ux-research/          # User experience research
├── marketing/            # Growth & marketing
├── sales/                # Sales operations
├── admin/                # Administrative support
├── accounting/           # Financial operations
├── media-production/     # Visual asset creation
└── contracting/          # Agent contracting & onboarding
```

## Usage

These agents are designed for [Claude Code](https://claude.com/claude-code) subagents and agent teams.

### Install globally
```bash
cp agents/**/*.md ~/.claude/agents/
```

### Enable Agent Teams
Add to `~/.claude/settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Using agents

**As subagents** — Claude automatically delegates to agents based on task context, or you can invoke them explicitly:
```
Use the ops-lead agent to diagnose my network issue
Have the security-auditor check this repo
```

**As a team** — Multiple agents work in parallel, communicate directly, and share a task list:
```
Create a team with fullstack-lead, qa-lead, and devops-lead to build and ship this feature
```

Each team has a **lead** (Opus) that coordinates and **specialists** (Sonnet) that execute. Leads create tasks, assign specialists, and synthesize results.

## Agent Format

Each `.md` file follows the Claude Code agent definition format:

```markdown
---
name: agent-name
description: One-line description
model: opus | sonnet
---

[System prompt with role, capabilities, methodology, and rules]
```
