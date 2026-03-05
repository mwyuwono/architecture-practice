# CLAUDE.md

This file defines coding-agent behavior for this repository.

## Documentation Authority Chain
Use documentation in this order:
1. `PRACTICE_MASTER.md` (practice-wide documentation authority)
2. `<project>/PROJECT_MASTER.md` (project documentation authority)
3. `<project>/agent.md` (coding-agent execution protocol for that project)

If files disagree, higher authority wins.

## Scope
- `PROJECT_MASTER.md` files hold project requirements, design decisions, and planning context.
- `agent.md` files hold only coding-agent workflow and execution rules.
- Avoid duplicating project narrative content inside `agent.md`.

## Git and Backup Behavior
Agents must follow the git hygiene protocol in `PRACTICE_MASTER.md`.

Minimum required workflow:
1. `git fetch origin --prune`
2. `git status -sb`
3. Make scoped changes
4. `git add -A`
5. `git commit -m "<concise milestone message>"`
6. `git push origin <branch>`
7. `git status -sb`

Never run destructive git commands unless explicitly requested by the user.

## Working Style
- Be concise and direct.
- Prefer small, reviewable changes.
- Keep repository structure explicit and predictable.
- Update cross-references when files move or are renamed.

## Repository Layout (Current)
- `PRACTICE_MASTER.md`: practice documentation authority
- `agents.md`: quick pointer for non-Claude agents
- `project-personal-cottage/`: active project folder
- `tools/`: shared tools/utilities
