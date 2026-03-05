# agent.md

Primary coding-agent instructions for this repository.
Designed to be discoverable by any coding agent (Claude, Cursor, Copilot, etc.).

Claude users: `CLAUDE.md` cross-references this file and adds Claude-specific loading behavior.

---

## Documentation Authority Chain

Use documentation in this order:

1. `PRACTICE_MASTER.md` — practice-wide documentation authority
2. `<project>/PROJECT_MASTER.md` — project documentation authority
3. `<project>/agent.md` — coding-agent execution protocol for that project

If files disagree, higher authority wins.

## Scope

- `PROJECT_MASTER.md` files hold project requirements, design decisions, and planning context.
- `agent.md` files hold only coding-agent workflow and execution rules.
- Avoid duplicating project narrative content inside `agent.md`.

## Git and Backup Behavior

Follow the git hygiene protocol in `PRACTICE_MASTER.md`.

Minimum required workflow:

1. `git fetch origin --prune`
2. `git status -sb`
3. Make scoped changes
4. `git add -A`
5. `git commit -m "<concise milestone message>"`
6. `git push origin <branch>`
7. `git status -sb`

Never run destructive git commands unless explicitly requested by the user.

### Session-Start Backup Check
At the start of each coding session, before substantive work:
1. Check backup readiness:
- `~/.config/arch-backup/backup.env` exists and has non-placeholder `S3_BUCKET`
- LaunchAgent `com.mwy.archbackup` is loaded (`launchctl print gui/$(id -u)/com.mwy.archbackup`)
- Last sync time from `~/.local/state/arch-backup/last_run_epoch` (if present)
2. Report a concise status line to the user (`active`/`inactive`, and last sync age if known).
3. If backup is inactive, unconfigured, or last sync is stale (>24h), explicitly ask whether to run backup now (typically `~/bin/arch_backup_on` and/or `~/bin/arch_backup_sync.sh`) before continuing.

## Working Style

- Be concise and direct.
- Prefer small, reviewable changes.
- Keep repository structure explicit and predictable.
- Update cross-references when files move or are renamed.

## Notes Ingestion Protocol

At the start of each session, before any other work:

### Step 1 — Scan
Check all `notes/` folders for files (ignore `.gitkeep`):
- `notes/` (practice-level)
- `<project>/notes/` for each project listed in the Project Index

If no notes are found, proceed normally.

### Step 2 — Interpret and Route
For each note file found, read the content and determine the appropriate target:

| Note Content | Typical Source | Target |
|---|---|---|
| Practice conventions, naming standards, documentation policy | `notes/` (root) | `PRACTICE_MASTER.md` |
| Design intent: massing, materials, style, orientation | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → Design Intent |
| Technical design decisions | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → Decision Log |
| Technical systems: HVAC, structural, envelope, MEP | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → relevant systems section, or new section |
| Client brief, space requirements, adjacencies | `<project>/notes/` | `<project>/Program/program.md` (create file if absent) |
| Site, survey, context | `<project>/notes/` | `<project>/Site/site-analysis.md` (create file if absent) |
| Code, zoning, jurisdiction | `<project>/notes/` | `<project>/Code_Research/<jurisdiction>-<code>-notes.md` |
| Permit, agency, approval | `<project>/notes/` | `<project>/Permits/` (create folder if absent) |
| Consultant coordination, RFI | `<project>/notes/` | `<project>/Coordination/` (create folder if absent) |
| Meeting, discussion, decision recap | `<project>/notes/` | `<project>/Meetings/YYYY-MM-DD_<topic>.md` (create folder if absent) |
| Historic, commission, or client-facing significance | `<project>/notes/` | `<project>/PROJECT_MASTER.md` → Notes of Record (create section if absent) |
| Agent execution or workflow changes | any | root `agent.md` or `<project>/agent.md` |
| Ambiguous or no clean fit | any | Propose target and rationale to user |

Integration style:
- Decision Log entries: `- YYYY-MM-DD: [interpreted content]`
- Section body additions: integrated prose, no date prefix
- New sections: include proposed section name and full content in the batch summary

### Step 3 — Present Batch Summary
Before writing anything, present a single batch summary showing for each note:
- Note filename and raw content
- Proposed target file and section
- Proposed text to be added

Wait for explicit user confirmation before proceeding.

### Step 4 — Write and Archive
After confirmation:
1. Write the interpreted content to each target file.
2. Create `processed-notes/` adjacent to the source `notes/` folder if it does not exist.
3. Move each note file into `processed-notes/`.
4. Commit all changes per the git hygiene protocol with a message like `Process notes from YYYY-MM-DD session`.

## Documentation Hygiene Protocol

### Update, Don't Append
When content changes, edit the existing section. Do not create a parallel section or a new file alongside the old one. If the prior version has archival value, move it to `Archive/` before editing.

### Archive, Don't Delete or Comment Out
Superseded content is never silently deleted or left commented out:
- Move to `Archive/YYYY-MM-DD_<reason>/` in the relevant project folder.
- Update any cross-references in other files to point to the archive or remove the stale reference.

### Plan File Lifecycle
After implementing a plan from `.claude/plans/`:
- Delete the plan file if fully implemented and no follow-up is needed.
- Move to `Archive/` if it contains useful historical context.
- Never leave stale plan files in `.claude/plans/`.

### Cross-Reference Sync
When renaming or moving a file or section:
- Search for references to it across `PROJECT_MASTER.md`, `agent.md`, `PRACTICE_MASTER.md`, and `Templates/`.
- Update or remove stale references before committing.

### No Duplicate Information
Before writing new content, check whether it already exists in `PROJECT_MASTER.md`, `PRACTICE_MASTER.md`, or the relevant spec or schedule. If it does, cross-reference instead.

## Repository Layout

- `PRACTICE_MASTER.md` — practice documentation authority
- `agent.md` — primary coding-agent instructions (this file)
- `CLAUDE.md` — Claude-specific supplement; cross-references this file
- `standards/` — shared technical standards (cross-referenced from project files)
- `project-personal-cottage/` — active project folder
- `tools/` — shared tools/utilities

## Project Index

| Project | Agent File | Project Master |
|---|---|---|
| Personal Cottage | `project-personal-cottage/agent.md` | `project-personal-cottage/PROJECT_MASTER.md` |

