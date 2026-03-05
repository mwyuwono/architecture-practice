# PROJECT_MASTER.md - Personal Cottage

## Project Scope and Authority
This file is the master documentation authority for the Personal Cottage project.

Cross-reference:
- Practice master: `../PRACTICE_MASTER.md`
- Coding-agent execution file: `agent.md`

Documentation boundary:
- Project requirements, design intent, constraints, and decisions belong here.
- `agent.md` contains only coding-agent operational guidance and workflow protocol.

## Project Overview
- Project Name: Personal Cottage
- Location: Massachusetts, Vermont, or Connecticut (exact municipality pending)
- Square Footage Goal: 2,500 SF
- Occupancy Type: Single-family residential
- Site Context: Rural setting
- Construction Quality: High-end residential construction
- Architectural Style Priority: Greek Revival (high priority)

## Design Intent and Constraints
- Preserve classical Greek Revival character in massing and detail hierarchy.
- Finish materials should prioritize natural materials and avoid synthetic substitutes that do not age similarly.
- Additional dimensional/code constraints are to be added as design progresses.

## Data and Deliverables Structure
- Drawings: `Drawings/`
- Raw extracts: `Data_Raw/` (source of truth for schedule data)
- Generated schedules: `Schedules/`
- Material/assembly specs: `Specs/`
- Code and zoning notes: `Code_Research/`

Naming conventions:
- Raw data: `YYYY-MM-DD_<source>_<topic>.csv|json`
- Schedules: `<discipline>-schedule.md`
- Specs: `<system>-spec.md`
- Code notes: `<jurisdiction>-<code>-notes.md`

## Code Research Status
- Jurisdiction is not fixed; all code compliance checks are currently provisional.
- Once municipality is selected, create jurisdiction-specific notes in `Code_Research/` and update required code pathways.

## Decision Log
- 2026-03-05: State 000 scaffold initialized.
- 2026-03-05: State 001 initialized with location shortlist (MA/VT/CT), 2,500 SF target, and Greek Revival + natural-aging material priorities.
- 2026-03-05: Added occupancy (single-family), construction target (high-end), and rural site assumption.
- 2026-03-05: Migrated project-level documentation authority from `agent.md` to `PROJECT_MASTER.md`.
