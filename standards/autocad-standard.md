# AutoCAD Drafting Standard

Practice-wide standard for plain AutoCAD 2D documentation. Applies to all projects unless a project's `PROJECT_MASTER.md` specifies an override.

AutoCAD is a drawing and documentation system, not BIM. Object metadata links are limited to blocks, attributes, fields, and data extraction workflows.

Drafting outcomes must prioritize:
- consistency across sheets and phases
- predictable plotting and exports
- easy global edits
- clear coordination with consultants
- low-risk file management

## Default Standards

1. Use NCS/AIA-style layer naming (discipline + major + minor): `A-WALL-FULL`, `A-DOOR`, `A-ANNO-TEXT`, `A-STRS`.
2. Use annotative scaling for text and dimensions where appropriate; otherwise enforce a consistent plotted text-height strategy.
3. Keep geometry in model space and sheets in paper space layouts with standardized viewport and plotting setups.
4. Use XREFs for coordinated backgrounds and SSM for multi-sheet metadata consistency.
5. Maintain CTB/STB plotting consistency so lineweights, screening, and linetypes remain predictable across all files.

## Decision Framework: When to Use What

### XREFs
Use when the same base geometry appears on multiple sheets, when consultant coordination is required, or when recurring backgrounds are needed.

Required pattern:
- one model file per level (or zone when project scale requires)
- sheet files consume model XREFs
- relative paths and shared origin at `0,0,0`

Do not copy/paste model geometry between sheet files.

### Dynamic Blocks
Use for repeated symbols with controlled variation (doors, windows, stair symbols, markers, furniture/equipment placeholders).

Required pattern:
- visibility states for graphics
- stretch parameters for dimensional variants
- clean geometry and layer discipline

Do not over-parameterize one-off geometry.

### Attributes
Use when symbols require structured, extractable metadata (door/window marks, stair IDs, keynotes, equipment tags).

Required pattern:
- stable ALL CAPS attribute schema
- correct annotation layers (e.g., `A-ANNO-TAGS`)
- schedule generation via `DATAEXTRACTION`
- QA checks for duplicates, missing values, and out-of-range values

### Fields + Sheet Set Manager (SSM)
Use for sheet numbers, titles, issue dates, revisions, and cross-references.

Required pattern:
- title block as a block with SSM field mapping
- one SSM per project

Avoid manual sheet metadata entry.

### Data Extraction
Use for frequently changing schedules (doors, windows, finishes, equipment).

Required pattern:
- project-managed `.dxe` definition
- table layer standards (`A-TABL` or `A-ANNO-TABL` per office convention)
- refresh extraction before milestone and issue sets

### Layer States
Use for sheet-variant visibility (permit/DD/CD, life safety, furniture, consultant overlays), paired with viewport overrides when needed.

## Coordination Rules for Common Elements

### Stairs
- Draft in 2D with explicit cut-vs-beyond conventions.
- Use a dedicated stair plan symbol block for treads/arrows/break lines.
- When scheduled, stair blocks must include attributes: `STAIR_ID`, `WIDTH`, `RISERS`, `RISER_HT`, `TREAD_DP`, `LANDING_DP`.
- Stair spec references remain keyed by note/keynote IDs.

### Doors and Windows
- Use dynamic blocks plus attributes when schedules are required.
- Keep insertion points and scaling behavior consistent.
- Separate plan/elevation blocks where representation differs.

### Grids, Levels, Section/Elevation Marks
- Use blocks consistently.
- Prefer attributes for IDs and fields for sheet/detail references when SSM is present.

## CAD Subfolders (inside `Drawings/`)
Create as the project scales; do not pre-create empty:

| Subfolder | Contents |
|---|---|
| `XREF/` | Model/reference files consumed by sheets |
| `Sheets/` | Sheet layout files |
| `Details/` | Detail drawings |
| `Library/` | Block libraries, standard symbols |
| `Exports/` | PDF/DWF/DXF issue exports |

Use relative paths. Maintain shared drawing origin at `0,0,0`.

## Do This, Not That

- XREF backgrounds — not copied geometry
- Dynamic blocks for repeated symbols — not manual redraws
- Attributes + data extraction for schedule-driven objects — not manual tables
- SSM + fields for sheet metadata — not manual typing
- Layer states/viewport overrides for visibility — not duplicated content

## Escalation Boundary (Plain AutoCAD vs BIM)
If bidirectional spec-object synchronization or model-driven intelligence is requested, treat it as out-of-scope for plain AutoCAD and evaluate BIM workflow adoption explicitly. For spec linkage in plain AutoCAD, use keynote IDs, hyperlinks, and attribute-driven schedules.
