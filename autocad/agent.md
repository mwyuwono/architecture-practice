# agent.md

## Project Overview
### Initial Project Identity
- Location: Massachusetts, Vermont, or Connecticut (exact municipality pending)
- Square Footage Goals: 2,500 SF target
- Architectural Style: Greek Revival

### Core Project Metadata
- Site Address: Pending (state-level shortlist only: MA/VT/CT)
- Climate Zone: Pending
- Occupancy Type: Single-family residential
- State Entry Status: State 001 initialized (identity draft captured; jurisdiction-specific code context pending)

## Design Logic & Constraints
- Record governing design rules and dimensional constraints here.
- Example: All exterior walls must be 6-inch nominal.
- Example: Minimum hallway clear width is 36 inches.
- Classical Greek Revival character is high-priority and should govern major massing/detail decisions.
- Finish materials should prioritize natural materials and avoid synthetic substitutes that do not weather/age similarly to natural materials.
- Construction quality target: high-end residential construction.
- Site context assumption: rural setting.

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
- 2026-03-05: State 001 initialized from user-provided identity. Set location shortlist (MA/VT/CT), target size (2,500 SF), and Greek Revival + natural-material aging preference as high-priority constraints.
- 2026-03-05: Updated project metadata with single-family occupancy, high-end construction target, and rural site setting.

## Operating Conventions
- Schedules file naming: `<discipline>-schedule.md`
- Specs file naming: `<system>-spec.md`
- Code research file naming: `<jurisdiction>-<code>-notes.md`
