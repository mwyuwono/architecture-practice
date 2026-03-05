# agent.md

## Project Overview
### Initial Project Identity
- Location: Pending
- Square Footage Goals: Pending
- Architectural Style: Pending

### Core Project Metadata
- Site Address: Pending
- Climate Zone: Pending
- Occupancy Type: Pending
- State Entry Status: Pending (awaiting initial identity details)

## Design Logic & Constraints
- Record governing design rules and dimensional constraints here.
- Example: All exterior walls must be 6-inch nominal.
- Example: Minimum hallway clear width is 36 inches.

## Data Source Mapping
- Source of truth: structured `.csv` and `.json` files stored in `/Data_Raw`.
- All values published to `/Schedules/*.md` must trace back to a named input file in `/Data_Raw`.
- If a schedule value conflicts with raw data, `/Data_Raw` supersedes derived schedule content.
- Preferred naming convention for raw files: `YYYY-MM-DD_<source>_<topic>.csv|json`.

## Verification Protocol
For every new design update or data drop, run this workflow:

1. Parse input:
- Extract dimensions, materials, counts, source file path, and update date.

2. Validate against internal constraints:
- Compare extracted values against entries in `Design Logic & Constraints`.

3. Cross-check against code research:
- Compare affected elements against notes in `/Code_Research/*.md`.
- Until jurisdiction/location is confirmed, mark code checks as `Provisional`.

4. Update downstream documents:
- Schedule-related changes: update `/Schedules/<discipline>-schedule.md`.
- Material/assembly changes: update `/Specs/<system>-spec.md`.

5. Conflict detection and alerting:
- If new data conflicts with a prior instruction or code note, log a conflict line with:
  - Type
  - Source
  - Prior Rule
  - New Data
  - Recommended Resolution

6. Record the decision:
- Append a dated entry to `Change Log` including rationale and affected files.

## Change Log
- 2026-03-05: State 000 scaffold initialized. Awaiting Project Identity details (Location, Square Footage Goals, Architectural Style).

## Operating Conventions
- Schedules file naming: `<discipline>-schedule.md`
- Specs file naming: `<system>-spec.md`
- Code research file naming: `<jurisdiction>-<code>-notes.md`
