# agent.md

## Purpose
This file is the coding-agent execution protocol for this project.
For repo-wide agent behavior, see `../agent.md`.

Notes ingestion: see `../agent.md` — Notes Ingestion Protocol. Check `notes/` at session startup per that protocol.
Documentation hygiene: see `../agent.md` — Documentation Hygiene Protocol.

Documentation authority:
- Project documentation authority: `PROJECT_MASTER.md`
- Practice documentation authority: `../PRACTICE_MASTER.md`
- Document taxonomy and routing: `../PRACTICE_MASTER.md` → Documentation Strategy

## Required Inputs for Agent Work
Before implementing changes, read:
1. `PROJECT_MASTER.md` for project requirements and decisions.
2. `Code_Research/*.md` for jurisdiction notes.
3. `Data_Raw/*.csv` and `Data_Raw/*.json` for schedule/spec source data.

## Operational Data Mapping
- Source of truth: `Data_Raw/*.csv`, `Data_Raw/*.json`
- Derived outputs:
  - `Schedules/*.md`
  - `Specs/*.md`
- Code notes source:
  - `Code_Research/*.md`

## Verification Protocol (Execution)
For each update or data drop:
1. Parse dimensions, materials, counts, source file, and date.
2. Validate against constraints in `PROJECT_MASTER.md`.
3. Cross-check code notes in `Code_Research/*.md`.
4. Update `Schedules/*.md` and/or `Specs/*.md`.
5. Report conflicts with:
- Type
- Source
- Prior Rule
- New Data
- Recommended Resolution
6. Append dated decision entry to `PROJECT_MASTER.md`.

## Git Hygiene
Follow `../PRACTICE_MASTER.md` git protocol.

Minimum:
- Check `git status -sb` before/after work.
- Commit and push at milestones.
- Leave a clean working tree unless user asks otherwise.
