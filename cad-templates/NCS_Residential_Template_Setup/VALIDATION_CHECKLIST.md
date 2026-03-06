# Validation Checklist

Use this checklist to verify the template is correctly configured before saving as DWT.

## Instructions

1. Open the configured drawing (after running script and manual steps)
2. Work through each section below
3. Mark items as PASS or FAIL
4. Fix any FAIL items before saving as template

---

## Units and System Variables

| Check | Expected | Command | Status |
|-------|----------|---------|--------|
| Linear units | Architectural | `UNITS` | ☐ |
| Linear precision | 1/16" (5) | `UNITS` | ☐ |
| Angular units | Decimal Degrees | `UNITS` | ☐ |
| Angular precision | 0 | `UNITS` | ☐ |
| Lineweight display | ON | `LWDISPLAY` (should = 1) | ☐ |
| Insertion units | Inches | `INSUNITS` (should = 1) | ☐ |

---

## Layers

### Layer Count

| Check | Expected | Command | Status |
|-------|----------|---------|--------|
| Total layer count | 21 layers | `LAYER` then count | ☐ |
| No unwanted layers | No: Title Block, A-Electrical, A-Plumbing, Reference, Elevation, Section AA, No Print | `LAYER` | ☐ |

### Layer Names (verify these exist)

| Layer | Exists | Status |
|-------|--------|--------|
| 0 | ☐ | |
| A-WALL | ☐ | |
| A-DOOR | ☐ | |
| A-WIND | ☐ | |
| A-FLOR | ☐ | |
| A-CLNG | ☐ | |
| A-ROOF | ☐ | |
| A-STRS | ☐ | |
| A-FURN | ☐ | |
| A-GLAZ | ☐ | |
| A-COLS | ☐ | |
| A-HATCH | ☐ | |
| A-VIEW | ☐ | |
| A-ANNO-DIMS | ☐ | |
| A-ANNO-TEXT | ☐ | |
| A-ANNO-SYMB | ☐ | |
| S-BEAM | ☐ | |
| S-COLS | ☐ | |
| C-GRID | ☐ | |
| V-VPRT | ☐ | |
| Defpoints | ☐ | |

### Layer Properties (spot check)

| Layer | Color | Linetype | LW (mm) | Plot | Status |
|-------|-------|----------|---------|------|--------|
| A-WALL | 1 | Continuous | 0.50 | Yes | ☐ |
| A-CLNG | 8 | Hidden | 0.18 | Yes | ☐ |
| C-GRID | 9 | Center | 0.18 | Yes | ☐ |
| V-VPRT | 8 | Continuous | Default | **No** | ☐ |

---

## Linetypes

| Linetype | Loaded | Command: `-LINETYPE` then `?` | Status |
|----------|--------|-------------------------------|--------|
| Continuous | ☐ | | |
| Hidden | ☐ | | |
| Center | ☐ | | |
| Phantom | ☐ | | |

---

## Text Styles

| Style | Exists | Font | Command: `STYLE` | Status |
|-------|--------|------|------------------|--------|
| ANNO-TEXT | ☐ | Arial | | |
| ANNO-TITLE | ☐ | Arial Black | | |

---

## Dimension Style

| Check | Expected | Command: `DIMSTYLE` | Status |
|-------|----------|---------------------|--------|
| ARCH-DIMS exists | Yes | | ☐ |
| ARCH-DIMS is current | Yes | | ☐ |
| Unit format | Architectural | Modify > Primary Units | ☐ |
| Precision | 1/16" | Modify > Primary Units | ☐ |
| Text style | ANNO-TEXT | Modify > Text | ☐ |
| Arrow size | 1/8" | Modify > Symbols | ☐ |
| Text height | 3/32" | Modify > Text | ☐ |

**Quick test:** Draw a test dimension and verify it displays correctly, then delete it.

---

## Annotation Scales

| Scale | In List | Command: `SCALELISTEDIT` | Status |
|-------|---------|--------------------------|--------|
| 1" = 1'-0" | ☐ | | |
| 3/4" = 1'-0" | ☐ | | |
| 1/2" = 1'-0" | ☐ | | |
| 3/8" = 1'-0" | ☐ | | |
| 1/4" = 1'-0" | ☐ | | |
| 3/16" = 1'-0" | ☐ | | |
| 1/8" = 1'-0" | ☐ | | |

---

## Layouts

| Check | Expected | Status |
|-------|----------|--------|
| ARCH-D-Starter layout exists | Yes | ☐ |
| Layout1 and Layout2 deleted | Yes | ☐ |
| Page setup configured | Paper size = ARCH D | ☐ |
| Plot scale | 1:1 | ☐ |
| Plot style table assigned | Yes (monochrome.ctb or custom) | ☐ |

---

## Drawing Cleanliness

| Check | Expected | Command | Status |
|-------|----------|---------|--------|
| No unwanted geometry in model space | Empty or minimal | Zoom Extents | ☐ |
| No geometry on Title Block layer | Layer deleted | Verify | ☐ |
| Current layer | 0 | `CLAYER` | ☐ |
| No orphaned objects | Clean | `AUDIT` | ☐ |
| No purgeable items | Clean | `PURGE` | ☐ |

---

## Functional Tests

### Test 1: Create a wall line

1. Set layer to A-WALL
2. Draw a line
3. Verify: Color = Red (1), Lineweight = 0.50mm
4. Delete the line

| Result | Status |
|--------|--------|
| Line displays correctly | ☐ |

### Test 2: Create a dimension

1. Set layer to A-ANNO-DIMS
2. Verify ARCH-DIMS is current style
3. Create a linear dimension on a test line
4. Verify: Architectural format, 1/16" precision, correct text style
5. Delete test objects

| Result | Status |
|--------|--------|
| Dimension displays correctly | ☐ |

### Test 3: Create a viewport

1. Switch to ARCH-D-Starter layout
2. Set layer to V-VPRT
3. Create a viewport with MVIEW
4. Verify viewport is on V-VPRT layer
5. Preview plot or check plot preview
6. Verify viewport boundary does NOT appear in plot preview

| Result | Status |
|--------|--------|
| Viewport on correct layer | ☐ |
| Viewport does not plot | ☐ |

---

## Final Verification

| Check | Status |
|-------|--------|
| All CRITICAL items pass | ☐ |
| All layer properties correct | ☐ |
| Dimension style works as expected | ☐ |
| Layout configured for plotting | ☐ |
| Drawing is clean and purged | ☐ |
| Ready to save as DWT | ☐ |

---

## Sign-Off

| Field | Value |
|-------|-------|
| Validated by | |
| Date | |
| AutoCAD version | |
| Template filename | |
| Notes | |
