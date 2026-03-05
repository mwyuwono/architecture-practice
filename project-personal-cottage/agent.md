# agent.md

Primary coding-agent instructions for the Personal Cottage project.
Discoverable by any coding agent. For repo-wide agent behavior, see `../agent.md`.

## Purpose
This file is the coding-agent execution protocol for the Personal Cottage project.

Notes ingestion: see root `../agent.md` — Notes Ingestion Protocol. Check `notes/` at session startup per that protocol.

Documentation authority:
- Project documentation authority: `PROJECT_MASTER.md` (design intent, decisions, project-specific overrides)
- Practice-wide AutoCAD drafting standard: `../standards/autocad-standard.md`
- Practice documentation authority: `../PRACTICE_MASTER.md`

## Required Inputs for Agent Work
Before implementing changes, read:
1. `PROJECT_MASTER.md` for project requirements and decisions.
2. Relevant files in `Code_Research/` for jurisdiction notes.
3. Relevant raw data in `Data_Raw/` when producing schedules/spec outputs.

## CAD Execution Decision Protocol
For CAD requests, treat `PROJECT_MASTER.md` as the drafting source of truth and execute with plain AutoCAD assumptions.

Runtime workflow:
1. Classify request type:
- drafting standards/setup
- repeated symbol/library work
- schedule/tagging metadata
- multi-sheet metadata/referencing
- schedule extraction/reporting
- visibility/overlay control
2. Select mechanism:
- XREF for shared backgrounds/coordination
- dynamic block for repeated variable symbols
- attributes for structured IDs/metadata
- fields + SSM for sheet/detail metadata
- data extraction for schedules/tables
- layer states for sheet-variant visibility
3. Deliver implementation-ready outputs:
- explicit layer names
- block and attribute schemas
- folder/path conventions
- command sequence or automation route when requested
4. Avoid BIM claims:
- do not imply automatic model-spec synchronization in plain AutoCAD
- keep spec linkage via keynotes, attributes, and extracted schedules

## Operational Data Mapping
- Source of truth for extracted data: `Data_Raw/*.csv`, `Data_Raw/*.json`
- Derived outputs:
  - `Schedules/*.md`
  - `Specs/*.md`
- Code notes source:
  - `Code_Research/*.md` (provisional until municipality is confirmed)

## Verification Protocol (Execution)
For each update or data drop:
1. Parse dimensions, materials, counts, source file, and date.
2. Validate against constraints in `PROJECT_MASTER.md`.
3. Cross-check against `Code_Research/*.md`.
4. Update `Schedules/*.md` and/or `Specs/*.md` as needed.
5. If conflicts exist, report:
- Type
- Source
- Prior Rule
- New Data
- Recommended Resolution
6. Append dated decision entry to `PROJECT_MASTER.md`.

## CAD QA and Conflict Reporting
For CAD requests, run these checks before reporting completion:
1. Layer naming validation:
- verify NCS/AIA-style conventions and expected discipline/major/minor groups
2. Attribute integrity:
- detect duplicate IDs
- detect missing required values
3. XREF integrity:
- verify relative pathing
- verify shared insertion origin at `0,0,0` where required
4. File hygiene:
- run/confirm audit and purge workflow according to office standard
5. Plot verification:
- confirm lineweight, linetype, and scale behavior in plotted output test

If conflicts exist, report using the existing format:
- Type
- Source
- Prior Rule
- New Data
- Recommended Resolution

## Git Hygiene
Follow the repository git protocol in `../PRACTICE_MASTER.md`.

At minimum:
- Check status before and after changes.
- Commit and push at each meaningful milestone.
- Keep the working tree clean at task completion unless user requests otherwise.

## Agent Change Log
- 2026-03-05: Refactored to remove duplicated project narrative content; retained coding-agent execution protocol only.
- 2026-03-05: Added primary-file header; cross-reference to `../agent.md` for repo-wide agent behavior.
- 2026-03-05: Added CAD execution decision protocol and CAD QA/conflict checks; retained `PROJECT_MASTER.md` as sole project standards authority.
