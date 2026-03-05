Build a starter AutoCAD template for a new residential architectural design project that opens cleanly in AutoCAD (including AutoCAD for Mac) with preconfigured layers and basic sheet setup, so I can avoid repeated project setup.

Deliverables
1) A DXF file named:
   Templates/Architectural_Starter_ArchD_AIA_NCS.dxf
2) A seed DXF used for generation:
   Templates/seed-archd-annotative.dxf

Requirements
A) Units & globals
- Imperial (inches)
- Display units: Architectural
- Set key sysvars in the DXF HEADER (and in the .SCR):
  - $ACADVER = AC1015
  - $MEASUREMENT = 0 (imperial)
  - $INSUNITS = 1 (inches)
  - $LUNITS = 2 (architectural)
  - $LUPREC = 4
  - $TEXTSIZE = 0.125 (1/8")
  - Dimension defaults: DIMTXT=0.125, DIMASZ=0.125, DIMSCALE=1
  - Current style defaults: $TEXTSTYLE=A-TEXT-STD, $DIMSTYLE=A-DIM-STD, $DIMTXSTY=A-TEXT-STD
  - Association default: $DIMASSOC=2
  - Linetype scale defaults: $LTSCALE=1, $CELTSCALE=1, $PSLTSCALE=1, $MSLTSCALE=1
  - Annotative defaults: $CANNOSCALE=1/4\"=1'-0\", $ANNOAUTOSCALE=0, $ANNOALLVISIBLE=0

E) Dimension & annotation standards
- Require two text styles in STYLE table:
  - A-TEXT-STD (non-annotative)
  - A-TEXT-ANNO (annotative)
- Require two dim styles in DIMSTYLE table:
  - A-DIM-STD (non-annotative baseline)
  - A-DIM-ANNO (annotative)
- Dim style property targets:
  - DIMTXT=0.125
  - DIMASZ=0.125
  - DIMGAP=0.0625
  - DIMCLRD=6, DIMCLRE=6, DIMCLRT=6
  - DIMLUNIT=architectural
  - A-DIM-STD uses DIMSCALE=1
  - A-DIM-ANNO is annotative (no manual DIMSCALE inflation)

B) Sheet setup (in modelspace)
- Include an Arch D border rectangle: 36" x 24"
- Include an inner margin rectangle offset 0.5" from the border
- Put border geometry on layer A-BORDER
- Include a simple title block zone in the lower right (approx 14" wide x 7.5" high) on layer A-TTLB
- Add placeholder TEXT labels in the title block zone: PROJECT, DRAWING TITLE, SHEET, DATE, SCALE

C) Layer standard
- Use AIA / NCS-style discipline prefixes and simple descriptive suffixes.
- Provide layers for Architecture (A-), Structure (S-), MEP (M-/P-/E-/FP-), and Site/Civil (C-).
- Include a NoPlot viewport layer and DEFPOINTS set to NoPlot.

D) Plot/graphics strategy
- Use CTB-friendly conventions:
  - Assign layer colors intentionally to map lineweight hierarchy (typical CTB workflows).
  - Lineweights set per layer (DXF group code 370).
  - Set plot flag on/off per layer (DXF group code 290).
- Include linetypes: Continuous, Dashed, Center, Hidden.
  - Ensure linetypes are defined in the DXF LTYPE table.


Layer inventory (minimum set)
Create at least these layers (names exactly as below), with reasonable color/linetype/lineweight defaults:

Utility / NoPlot
- 0 (Continuous, plottable, lw ~0.25mm)
- DEFPOINTS (Continuous, NoPlot, lw 0.00)
- A-NPLT-VIEWPORT (Continuous, NoPlot, lw 0.00)
- A-REFR-XREF (Continuous, NoPlot, lw 0.00)

Architecture
- A-WALL (heavy)
- A-WALL-OTLN (heavy/medium heavy)
- A-DOOR (medium)
- A-WIND (medium)
- A-GLAZ (light)
- A-ROOF (medium)
- A-FLOR (medium)
- A-CLNG (light)
- A-STAIR (medium)
- A-CASE (light)
- A-FIXT (light)
- A-FURN (very light)
- A-EQPM (very light)
- A-HATCH (very light)
- A-OVERHD (Hidden, very light)
- A-CNTR (Center, very light)
Annotation / Sheet
- A-ANNO-TEXT
- A-ANNO-DIMS
- A-ANNO-TAGS
- A-ANNO-KEYN
- A-ANNO-NOTE
- A-ANNO-GRID (Center)
- A-BORDER
- A-TTLB

Structure
- S-COL (heavy)
- S-BEAM (heavy)
- S-SLAB (medium)
- S-FOUND (heavy)
- S-REINF (light)
- S-ANNO

Mechanical / Plumbing / Electrical / Fire Protection
- M-SPLY (medium)
- M-RETN (medium)
- M-DIFF (light)
- M-EQPM (light)
- M-ANNO
- P-PIPE (medium)
- P-FIXT (light)
- P-ANNO
- E-POWR (medium)
- E-LITE (light)
- E-LOWV (light)
- E-ANNO
- FP-PIPE (medium)
- FP-HEAD (light)
- FP-ANNO

Site/Civil
- C-TOPO (very light)
- C-ROAD (medium)
- C-PLNT (light)
- C-ANNO

Lineweight targets (use these exact values)
Use plotted lineweights (mm):
- heavy: 0.60
- medium: 0.35
- light: 0.18
- very light: 0.13
- title/border: 0.35 (border), 0.18 (title block text/lines)
For DXF, lineweight is stored in hundredths of mm as an integer (e.g., 0.35mm -> 35).

Color mapping (use a simple, standard CTB-friendly scheme)
- heavy: color 1
- medium: color 2
- light: color 3
- very light: color 4
- text/notes/tags: color 5
- dims: color 6
- border/title: color 7
- no-plot: color 8 or 9

DXF structure requirements
- Write a valid DXF with at minimum:
  SECTION: HEADER, TABLES (LTYPE, LAYER, STYLE, DIMSTYLE), ENTITIES, EOF
- Generation method: AC1032 seed-based pipeline.
  - Load a validated seed DXF and update layers, styles, dimstyles, and template geometry.
  - Preserve seed OBJECTS/LAYOUT scaffolding for maximum AutoCAD compatibility.
- Include LTYPE records for Continuous/Dashed/Center/Hidden.
- Include LAYER table records with:
  - name (code 2)
  - color (code 62)
  - linetype name (code 6)
  - plot flag (code 290)
  - lineweight (code 370)
- Include STYLE records for A-TEXT-STD and A-TEXT-ANNO.
- Include DIMSTYLE records for A-DIM-STD and A-DIM-ANNO.

Acceptance criteria additions
- HEADER includes exact values for:
  - $DIMSTYLE, $TEXTSTYLE, $DIMTXSTY, $DIMASSOC
  - $CANNOSCALE, $ANNOAUTOSCALE, $ANNOALLVISIBLE
  - $LTSCALE, $CELTSCALE, $PSLTSCALE, $MSLTSCALE
- A-DIM-STD is current by default in the template.
- Manual smoke in AutoCAD:
  - dimensions created with A-DIM-STD keep fixed non-annotative behavior
  - dimensions created with A-DIM-ANNO follow annotation scale behavior
- Annotative metadata integrity:
  - A-DIM-ANNO must preserve seed dimstyle metadata signature (table/xdata signature comparison).
  - Include a strict verification mode that fails if the annotative signature cannot be confirmed.

Generator CLI
- Primary generation:
  - python3 autocad/generate_archd_template.py
- Verification:
  - python3 autocad/generate_archd_template.py --verify
- Custom seed:
  - python3 autocad/generate_archd_template.py --seed autocad/Templates/seed-archd-annotative.dxf --verify
- Strict annotative verification:
  - python3 autocad/generate_archd_template.py --verify --strict-annotative


Output
- Provide the generated file in the local project folder and print the file paths at the end.
