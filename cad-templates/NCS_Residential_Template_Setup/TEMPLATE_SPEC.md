# NCS Residential Template Specification

Complete specification of the intended final state of the template after running `SETUP_SCRIPT.scr` and completing manual configuration.

## Drawing Configuration

### Units and Precision

| Setting | Value |
|---------|-------|
| Linear units | Architectural |
| Linear precision | 1/16" |
| Angular units | Decimal Degrees |
| Angular precision | 0 |
| Insertion scale | Inches |

### Drawing Environment

| Setting | Value |
|---------|-------|
| Lineweight display | ON |
| Drawing limits | Default (unlimited) |
| LTSCALE | 1 (annotative scaling preferred) |

## Layer Structure

### Architectural Layers (A-)

| Layer | Color | Linetype | Lineweight | Plot | Purpose |
|-------|-------|----------|------------|------|---------|
| A-WALL | 1 (Red) | Continuous | 0.50mm | Yes | Walls, major cut elements |
| A-DOOR | 30 (Orange) | Continuous | 0.35mm | Yes | Doors |
| A-WIND | 40 (Yellow-orange) | Continuous | 0.35mm | Yes | Windows |
| A-FLOR | 8 (Gray) | Continuous | 0.18mm | Yes | Floor patterns, finishes |
| A-CLNG | 8 (Gray) | Hidden | 0.18mm | Yes | Ceiling lines above |
| A-ROOF | 3 (Green) | Continuous | 0.35mm | Yes | Roof elements |
| A-STRS | 4 (Cyan) | Continuous | 0.35mm | Yes | Stairs, railings |
| A-FURN | 8 (Gray) | Continuous | 0.18mm | Yes | Furniture, equipment |
| A-GLAZ | 5 (Blue) | Continuous | 0.25mm | Yes | Glazing |
| A-COLS | 1 (Red) | Continuous | 0.50mm | Yes | Architectural columns |
| A-HATCH | 252 (Lt Gray) | Continuous | 0.09mm | Yes | Hatch patterns |
| A-VIEW | 6 (Magenta) | Continuous | 0.25mm | Yes | Section/elevation marks |

### Annotation Layers (A-ANNO-)

| Layer | Color | Linetype | Lineweight | Plot | Purpose |
|-------|-------|----------|------------|------|---------|
| A-ANNO-DIMS | 7 (White) | Continuous | 0.18mm | Yes | Dimensions |
| A-ANNO-TEXT | 7 (White) | Continuous | 0.18mm | Yes | Notes, labels |
| A-ANNO-SYMB | 7 (White) | Continuous | 0.18mm | Yes | Symbols, tags |

### Structural Layers (S-)

| Layer | Color | Linetype | Lineweight | Plot | Purpose |
|-------|-------|----------|------------|------|---------|
| S-BEAM | 10 (Red) | Continuous | 0.35mm | Yes | Structural beams |
| S-COLS | 10 (Red) | Continuous | 0.50mm | Yes | Structural columns |

### Coordination Layers (C-)

| Layer | Color | Linetype | Lineweight | Plot | Purpose |
|-------|-------|----------|------------|------|---------|
| C-GRID | 9 (Lt Gray) | Center | 0.18mm | Yes | Column grid |

### Support Layers

| Layer | Color | Linetype | Lineweight | Plot | Purpose |
|-------|-------|----------|------------|------|---------|
| 0 | 7 (White) | Continuous | Default | Yes | Default layer |
| V-VPRT | 8 (Gray) | Continuous | Default | **No** | Viewport boundaries |
| Defpoints | 7 (White) | Continuous | Default | No | System-managed |

## Linetypes

### Required Linetypes

| Linetype | Source | Usage |
|----------|--------|-------|
| Continuous | Built-in | Default for most elements |
| Hidden | acad.lin | Ceiling, hidden elements |
| Center | acad.lin | Grid lines, centerlines |
| Phantom | acad.lin | Future work, demolition |

## Text Styles

### ANNO-TEXT

| Property | Value |
|----------|-------|
| Font | Arial (fallback: Arial Narrow) |
| Height | 0 (controlled by text object) |
| Width factor | 1.0 |
| Oblique angle | 0 |
| Annotative | No (can be enabled per office preference) |

### ANNO-TITLE

| Property | Value |
|----------|-------|
| Font | Arial Black (fallback: Arial) |
| Height | 0 (controlled by text object) |
| Width factor | 1.0 |
| Oblique angle | 0 |
| Annotative | No |

## Dimension Style: ARCH-DIMS

### Primary Units

| Property | Value |
|----------|-------|
| Unit format | Architectural |
| Precision | 1/16" |
| Fraction format | Diagonal |
| Decimal separator | . |

### Lines

| Property | Value |
|----------|-------|
| Extension line offset | 1/16" |
| Extension beyond dim | 1/8" |
| Baseline spacing | 3/8" |
| Dimension line LW | 0.35mm |
| Extension line LW | 0.18mm |

### Symbols and Arrows

| Property | Value |
|----------|-------|
| Arrow type | Closed filled |
| Arrow size | 1/8" |

### Text

| Property | Value |
|----------|-------|
| Text style | ANNO-TEXT |
| Text height | 3/32" |
| Text placement | Above dimension line |
| Text gap | 1/16" |
| Text alignment | Horizontal |

## Annotation Scales

The following scales should be available in the scale list:

| Scale | Ratio |
|-------|-------|
| 1" = 1'-0" | 1:12 |
| 3/4" = 1'-0" | 1:16 |
| 1/2" = 1'-0" | 1:24 |
| 3/8" = 1'-0" | 1:32 |
| 1/4" = 1'-0" | 1:48 |
| 3/16" = 1'-0" | 1:64 |
| 1/8" = 1'-0" | 1:96 |

## Layouts

### ARCH-D-Starter

| Property | Target Value |
|----------|--------------|
| Paper size | ARCH D (24" x 36") |
| Plot area | Layout |
| Plot scale | 1:1 |
| Plot style table | monochrome.ctb (or office standard) |

## Model Space Organization

### Principles

1. All geometry drawn at 1:1 (full scale) in model space
2. Floor plans positioned near origin (0,0)
3. Elevations and sections placed to the side of plans
4. Details grouped separately

### Multi-Story Projects

Option A: Vertical separation
- Ground floor at Z=0
- Upper floors at Z=12' (or actual floor height)
- Use 3D orbit to navigate

Option B: Horizontal separation
- Ground floor near origin
- Upper floors offset 200'+ in X direction
- Easier for 2D-only workflows

Option C: Separate files with XREFs (recommended for larger projects)
- One DWG per floor
- Sheet files XREF model files
- Enables concurrent editing

## NCS Naming Logic

This template uses a simplified NCS-inspired naming convention:

```
[Discipline]-[Major][-Minor]

Discipline codes:
  A = Architectural
  S = Structural
  C = Coordination
  V = Viewport/support

Major groups:
  WALL, DOOR, WIND, FLOR, CLNG, ROOF, STRS, FURN, GLAZ, COLS, HATCH, VIEW
  ANNO (with -DIMS, -TEXT, -SYMB minors)
  BEAM, COLS (structural)
  GRID (coordination)
  VPRT (viewport)
```

This is intentionally simplified for residential work. Full NCS compliance would include status codes (N/E/D) and additional modifiers.

## Title Block Requirements

Title blocks are not included in the template. When creating or inserting a title block, include fields for:

- Project name
- Client name
- Project address
- Sheet number
- Sheet title
- Scale(s)
- Date
- Drawn by initials
- Checked by initials
- Revision history

Place title block content on A-ANNO-TEXT or a dedicated title block layer.
