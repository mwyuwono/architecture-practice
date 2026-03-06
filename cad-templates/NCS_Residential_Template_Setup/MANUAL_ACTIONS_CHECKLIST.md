# Manual Actions Checklist

Complete these steps after running `SETUP_SCRIPT.scr`. Items are organized by category and criticality.

## Pre-Flight Check

Before starting manual configuration, verify the script completed successfully:

- [ ] No error messages visible in command line history
- [ ] Layer list shows NCS-style names (A-WALL, A-DOOR, etc.)
- [ ] Title Block layer and content have been removed
- [ ] Drawing is clean (no unwanted geometry)

---

## Critical: Must Complete

### 1. Verify Dimension Style

The script creates ARCH-DIMS but dimension styles can be finicky in scripts.

**Steps:**
1. Type `DIMSTYLE` and press Enter
2. Verify ARCH-DIMS exists and is current
3. Click "Modify..." to check settings:
   - Primary Units tab: Architectural, 1/16" precision
   - Text tab: Text style = ANNO-TEXT, Height = 3/32"
   - Symbols and Arrows tab: Arrow size = 1/8"

**If settings are wrong:**
1. Modify ARCH-DIMS manually with correct values
2. Or delete and recreate using the settings in TEMPLATE_SPEC.md

### 2. Configure Annotation Scales

AutoCAD scripts cannot reliably modify the scale list.

**Steps:**
1. Type `SCALELISTEDIT` and press Enter
2. Delete unneeded metric scales (if present)
3. Add these scales if missing:
   - 1" = 1'-0"
   - 3/4" = 1'-0"
   - 1/2" = 1'-0"
   - 3/8" = 1'-0"
   - 1/4" = 1'-0"
   - 3/16" = 1'-0"
   - 1/8" = 1'-0"
4. Click OK

### 3. Configure Page Setup (ARCH-D-Starter Layout)

Page setup is machine-dependent and must be configured manually.

**Steps:**
1. Click the ARCH-D-Starter layout tab
2. Right-click the tab > Page Setup Manager
3. Click "Modify..."
4. Configure:
   - Printer/plotter: Select your PDF printer or plotter
   - Paper size: ARCH D (24.00 x 36.00 Inches)
   - Plot area: Layout
   - Plot scale: 1:1
   - Plot style table: monochrome.ctb (or office standard)
   - Plot options: ☑ Plot with lineweights
5. Click OK, then Close

---

## Important: Recommended

### 4. Verify Text Style Fonts

The script specifies Arial and Arial Black, which should be available on Mac.

**Steps:**
1. Type `STYLE` and press Enter
2. Select ANNO-TEXT, verify font is Arial
3. Select ANNO-TITLE, verify font is Arial Black
4. If fonts show as missing, substitute with available sans-serif fonts

**Recommended Mac fonts if needed:**
- Helvetica (system font, always available)
- Helvetica Neue
- SF Pro (may require macOS Monterey+)

### 5. Verify Layer Properties

Spot-check a few layers to confirm properties were applied.

**Steps:**
1. Type `LAYER` and press Enter (or click Layer Properties)
2. Check these layers:
   - A-WALL: Color 1, Continuous, 0.50mm, Plot=Yes
   - A-CLNG: Color 8, Hidden, 0.18mm, Plot=Yes
   - C-GRID: Color 9, Center, 0.18mm, Plot=Yes
   - V-VPRT: Color 8, Continuous, Plot=**No**
3. Correct any discrepancies manually

### 6. Assign Plot Style Table

If using named plot styles (STB) instead of color-dependent (CTB):

**Steps:**
1. Type `CONVERTPSTYLES` to switch between CTB and STB mode
2. Or: In Page Setup, select appropriate .stb file

---

## Optional: Enhancements

### 7. Create Additional Layouts

The script creates one starter layout. Add more as needed:

**Steps:**
1. Right-click ARCH-D-Starter tab
2. Select "New Layout"
3. Name appropriately (e.g., A101-FloorPlan, A201-Elevations)
4. Configure page setup for each

### 8. Set Up Viewport on Starter Layout

**Steps:**
1. Activate ARCH-D-Starter layout
2. Delete default viewport if present
3. Set current layer to V-VPRT
4. Draw viewport using MVIEW command
5. Double-click inside viewport to activate
6. Set scale (e.g., 1/4" = 1'-0")
7. Double-click outside viewport to deactivate

### 9. Import Title Block

**Steps:**
1. Obtain or create office standard title block
2. INSERT the block into paper space on the layout
3. Position at 0,0 (lower-left of printable area)
4. Configure any attribute fields

### 10. Save Layer States

After configuring layers, consider saving layer states for common views:

**Steps:**
1. Type `LAYERSTATE` and press Enter
2. Click "New..."
3. Create states like:
   - PLAN-ALL (all layers on)
   - PLAN-BASE (furniture, hatch off)
   - REFLECTED-CEILING (walls, ceiling, grid only)
4. Click Save

---

## Final Steps

### 11. Purge and Audit

**Steps:**
1. Type `PURGE` > Purge All > confirm
2. Type `AUDIT` > Fix errors = Yes
3. Type `REGEN`

### 12. Save as Template

**Steps:**
1. File > Save As
2. Format: Drawing Template (*.dwt)
3. Filename: `NCS_Residential_Template.dwt`
4. Location: Your templates folder
5. Add description: "NCS-style residential architectural template"

---

## Checklist Summary

| Item | Category | Status |
|------|----------|--------|
| Verify dimension style | Critical | ☐ |
| Configure annotation scales | Critical | ☐ |
| Configure page setup | Critical | ☐ |
| Verify text style fonts | Important | ☐ |
| Verify layer properties | Important | ☐ |
| Assign plot style table | Important | ☐ |
| Create additional layouts | Optional | ☐ |
| Set up viewport | Optional | ☐ |
| Import title block | Optional | ☐ |
| Save layer states | Optional | ☐ |
| Purge and audit | Final | ☐ |
| Save as template | Final | ☐ |
