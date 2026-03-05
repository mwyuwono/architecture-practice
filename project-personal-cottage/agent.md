# agent.md

## Purpose
This file is the coding-agent execution protocol for the Personal Cottage project.

Documentation authority:
- Project documentation authority: `PROJECT_MASTER.md`
- Practice documentation authority: `../PRACTICE_MASTER.md`

## Required Inputs for Agent Work
Before implementing changes, read:
1. `PROJECT_MASTER.md` for project requirements and decisions.
2. Relevant files in `Code_Research/` for jurisdiction notes.
3. Relevant raw data in `Data_Raw/` when producing schedules/spec outputs.

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

## Git Hygiene
Follow the repository git protocol in `../PRACTICE_MASTER.md`.

At minimum:
- Check status before and after changes.
- Commit and push at each meaningful milestone.
- Keep the working tree clean at task completion unless user requests otherwise.

## Agent Change Log
- 2026-03-05: Refactored to remove duplicated project narrative content; retained coding-agent execution protocol only.
