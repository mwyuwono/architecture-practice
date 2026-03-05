# PRACTICE_MASTER.md

## Purpose
This file is the master documentation index and operating manual for the entire architecture practice.

Documentation boundary:
- Project planning, design intent, standards, and decisions belong in this file and each project's `PROJECT_MASTER.md`.
- `agent.md` files remain the single source of truth for coding-agent execution behavior and automation workflow.

## Canonical References
- Coding agent primary instructions: `agent.md` (all agents)
- Claude supplement: `CLAUDE.md` (cross-references `agent.md`)
- Practice master documentation: `PRACTICE_MASTER.md` (this file)

## Practice Documentation Model
For each project under this repository:
1. Create `<project>/PROJECT_MASTER.md` as the project documentation authority.
2. Keep `<project>/agent.md` focused on coding-agent operations.
3. Keep only minimal project summary in `agent.md` that is required for automation safety.
4. When a drafting standard or technical policy applies to more than one project, extract it from `PROJECT_MASTER.md` into `standards/` at the practice root and cross-reference from each project.

## Documentation Strategy

Each piece of information has exactly one canonical home. Cross-reference rather than duplicate.

### Practice-Level Taxonomy

| File / Folder | Contents |
|---|---|
| `PRACTICE_MASTER.md` | Practice authority: standards, conventions, project index, documentation strategy |
| `agent.md` | Coding-agent execution protocol |
| `CLAUDE.md` | Claude-specific supplement only |
| `notes/` | Raw unprocessed notes (drop zone) |
| `standards/` | Shared technical standards applicable across all projects |
| `tools/` | Shared utilities and scripts |

### Project-Level Taxonomy

**Required at project initialization:**

| Folder / File | Contents |
|---|---|
| `PROJECT_MASTER.md` | Project authority: design intent, overview, decisions, drafting standards |
| `agent.md` | Project coding-agent execution protocol |
| `notes/` | Raw unprocessed notes |
| `processed-notes/` | Archived raw notes after ingestion |
| `Drawings/` | CAD files (DWG, DXF) |
| `Specs/` | Material and assembly specifications |
| `Schedules/` | Generated schedules |
| `Code_Research/` | Jurisdiction and code analysis notes |
| `Data_Raw/` | Source data for schedule generation |
| `Templates/` | Reusable document templates |
| `Archive/` | Superseded documentation |

**Create when first needed — never pre-create empty:**

| Folder | Create when |
|---|---|
| `Program/` | Client brief or space program is formalized |
| `Site/` | Site documentation is collected |
| `Permits/` | Permitting process begins |
| `Coordination/` | Consultants are engaged |
| `Meetings/` | Formal meeting notes need tracking |

### Document Routing Table

| Document Type | Canonical Location | Naming Convention |
|---|---|---|
| Design intent and constraints | `PROJECT_MASTER.md` → Design Intent | — |
| Technical design decisions | `PROJECT_MASTER.md` → Decision Log | `- YYYY-MM-DD: ...` |
| Practice-wide drafting standards | `standards/<standard>.md` | `autocad-standard.md` |
| Project-specific drafting overrides | `PROJECT_MASTER.md` → AutoCAD Drafting Standard | — |
| Client brief / space program | `Program/program.md` | — |
| Site analysis | `Site/site-analysis.md` | — |
| Material / assembly specifications | `Specs/<system>-spec.md` | `exterior-wall-spec.md` |
| Raw schedule source data | `Data_Raw/` | `YYYY-MM-DD_<source>_<topic>.csv` |
| Generated schedules | `Schedules/<type>-schedule.md` | `door-schedule.md` |
| Code / zoning / jurisdiction notes | `Code_Research/` | `<jurisdiction>-<code>-notes.md` |
| Permit documents and approvals | `Permits/` | `YYYY-MM-DD_<type>.md` |
| Consultant transmittals and RFIs | `Coordination/` | `YYYY-MM-DD_<consultant>_<topic>.md` |
| Meeting notes | `Meetings/` | `YYYY-MM-DD_<topic>.md` |
| Superseded documentation | `Archive/YYYY-MM-DD_<reason>/` | Dated subfolder |
| Raw notes (unprocessed) | `notes/` | Processed by agent at session start |

### Archive Policy

- Move superseded files to `Archive/YYYY-MM-DD_<reason>/` — never silently delete or comment out.
- When a phase closes, archive its deliverables as a batch with a descriptive subfolder name.
- Plan files (`.claude/plans/*.md`) are deleted or archived after implementation.
- Do not leave empty `Archive/` subfolders.

### Agent Writing Standards

1. No preamble. Start with content. Never write "This section describes..." or "It is worth noting that..."
2. Bullets over prose for reference material. Prose only for narrative sections (Design Intent, site analysis).
3. One truth per place. If information exists elsewhere, cross-reference — never copy.
4. Decision Log entries: one line, `- YYYY-MM-DD: factual statement`.
5. No orphaned section headers. Remove headers with no content.
6. If a section exceeds ~20 bullets or ~500 words, extract it to its own file and cross-reference.

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

