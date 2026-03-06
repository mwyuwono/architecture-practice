# AutoCAD Templates Guide

This is the single source of truth for creating and maintaining templates in this folder.

## Folder Layout
- `cad-templates/Architectural_Starter_ArchD_AIA_NCS.dxf`: generated template output (primary deliverable)
- `cad-templates/Architectural_Starter_ArchD_AIA_NCS.dwg`: DWG counterpart (manually exported from DXF in AutoCAD)
- `cad-templates/seed-archd-annotative.dxf`: seed used to preserve AC1032 scaffolding and annotative metadata
- `project-personal-cottage/generate_archd_template.py`: generator/verifier script

## Generation Workflow
1. From repo root, activate venv: `source project-personal-cottage/.venv/bin/activate`
2. Ensure dependency is installed in that venv: `pip install ezdxf`
3. Generate template: `python3 project-personal-cottage/generate_archd_template.py`
4. Verify template: `python3 project-personal-cottage/generate_archd_template.py --verify`
5. Strict annotative check: `python3 project-personal-cottage/generate_archd_template.py --verify --strict-annotative`
6. Optional custom seed: `python3 project-personal-cottage/generate_archd_template.py --seed cad-templates/seed-archd-annotative.dxf --verify`

## Required Technical Baseline
- DXF target: `AC1032` (AutoCAD 2018)
- Pipeline: seed-based (`ezdxf.readfile(seed)`) with controlled updates
- Units: imperial inches (`$MEASUREMENT=0`, `$INSUNITS=1`)
- Display units: architectural (`$LUNITS=2`)
- Core styles:
  - Text: `A-TEXT-STD`, `A-TEXT-ANNO`
  - Dim: `A-DIM-STD`, `A-DIM-ANNO`
- Current defaults:
  - `$TEXTSTYLE=A-TEXT-STD`
  - `$DIMSTYLE=A-DIM-STD`
  - `$DIMTXSTY=A-TEXT-STD`
  - `$DIMASSOC=2`

## Annotative Safety Rules
- Do not hand-edit raw DXF tags.
- Do not replace the seed with a minimal DXF.
- Keep `A-DIM-ANNO` derived from the seed dimstyle metadata signature.
- If optional annotative header vars are unavailable through API (`$CANNOSCALE`, `$ANNOAUTOSCALE`, `$ANNOALLVISIBLE`, `$MSLTSCALE`), rely on seed/object-level metadata and keep verification warnings visible.

## Geometry + Layer Minimums
- Arch D border in modelspace: `36" x 24"`
- Inner margin offset: `0.5"`
- Title block zone lower-right: approximately `14" x 7.5"`
- Title block labels: `PROJECT`, `DRAWING TITLE`, `SHEET`, `DATE`, `SCALE`
- Maintain required AIA/NCS-style layer inventory and lineweight/color mapping used by the generator.

## Change Control
- Any template standard change must update both:
  - `project-personal-cottage/generate_archd_template.py`
  - this `cad-templates/TEMPLATE-GUIDE.md`
- Regenerate and run `--verify` before commit.
- If `--verify` warns that the DWG counterpart is missing or stale, re-export `cad-templates/Architectural_Starter_ArchD_AIA_NCS.dwg` from the generated DXF.
- Validate openability in AutoCAD for Mac before release.
