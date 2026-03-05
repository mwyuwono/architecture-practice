# PRACTICE_MASTER.md

## Purpose
This file is the master documentation index and operating manual for the entire architecture practice.

Documentation boundary:
- Project planning, design intent, standards, and decisions belong in this file and each project's `PROJECT_MASTER.md`.
- `agent.md` files remain the single source of truth for coding-agent execution behavior and automation workflow.

## Canonical References
- Coding agent global instructions: `CLAUDE.md`
- Agent compatibility pointer: `agents.md`
- Practice master documentation: `PRACTICE_MASTER.md` (this file)

## Practice Documentation Model
For each project under this repository:
1. Create `<project>/PROJECT_MASTER.md` as the project documentation authority.
2. Keep `<project>/agent.md` focused on coding-agent operations.
3. Keep only minimal project summary in `agent.md` that is required for automation safety.

## Project Index
| Project | Path | Project Master | Agent File |
|---|---|---|---|
| Personal Cottage | `project-personal-cottage/` | `project-personal-cottage/PROJECT_MASTER.md` | `project-personal-cottage/agent.md` |

## Git Backup and Working Tree Hygiene Protocol (for Coding Agents)
Agents must proactively keep work backed up and the tree tidy.

### Startup Checks (every session)
1. `git fetch origin --prune`
2. `git status -sb`
3. Confirm active branch and remote tracking are expected.

### Before Mutating Files
1. Confirm there are no unexpected unrelated changes.
2. If unexpected changes are present, pause and request user direction.
3. Never use destructive commands (`git reset --hard`, `git checkout --`) unless explicitly requested.

### Proactive Backup Cadence
1. Commit and push at each meaningful milestone or at least every 45-60 minutes during active editing.
2. Use clear commit messages that describe the actual structural or functional change.
3. Push immediately after each milestone commit.

### Clean Tree Rule
1. End each completed task with either:
- a clean working tree, or
- a clearly stated list of intentional uncommitted changes.
2. Do not leave partially staged or ambiguous state.

### Recommended Agent Command Sequence
1. `git status -sb`
2. `git add -A`
3. `git commit -m "<concise milestone message>"`
4. `git push origin <branch>`
5. `git status -sb`

### Large or Risky Changes
1. Prefer smaller commits over one large commit.
2. If reorganization is large, explicitly verify file moves/renames before commit.
3. Confirm push success and resulting branch state (`ahead/behind`).

## Practice-Level Conventions
- Keep project-specific docs inside project folders.
- Use explicit filenames:
  - `PROJECT_MASTER.md` for project documentation authority.
  - `agent.md` for coding-agent operations.
- Keep decisions chronological in each project master file.

## Change Log
- 2026-03-05: Established practice-wide documentation architecture and coding-agent git hygiene protocol.
