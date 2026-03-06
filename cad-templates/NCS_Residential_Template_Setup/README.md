# NCS Residential Template Setup Package

A template setup package for AutoCAD for Mac, configured for residential architectural drafting using NCS/UDS-inspired naming conventions.

## Package Contents

| File | Purpose |
|------|---------|
| `README.md` | This file - setup instructions and usage guide |
| `TEMPLATE_SPEC.md` | Complete specification of the final template state |
| `LAYER_SCHEDULE.csv` | Layer definitions with all properties |
| `SETUP_SCRIPT.scr` | AutoCAD script for automated configuration |
| `MANUAL_ACTIONS_CHECKLIST.md` | Steps requiring manual AutoCAD work |
| `VALIDATION_CHECKLIST.md` | QA checklist before saving as DWT |
| `ASSUMPTIONS_AND_LIMITATIONS.md` | Mac-specific notes and caveats |

## Quick Start

### Prerequisites

- AutoCAD for Mac (2020 or later recommended)
- The starter template file: `starter-template.dxf`

### Setup Sequence

1. **Open the starter template**
   - Launch AutoCAD for Mac
   - Open `starter-template.dxf`

2. **Run the setup script**
   - Type `SCRIPT` at the command line and press Enter
   - Navigate to and select `SETUP_SCRIPT.scr`
   - Wait for the script to complete (watch the command line for progress)

3. **Complete manual steps**
   - Follow `MANUAL_ACTIONS_CHECKLIST.md` for:
     - Annotation scale configuration
     - Page setup
     - Plot style assignment

4. **Validate the template**
   - Use `VALIDATION_CHECKLIST.md` to verify all settings

5. **Save as template**
   - File > Save As
   - Change format to Drawing Template (*.dwt)
   - Save as `NCS_Residential_Template.dwt`

## What the Script Does

### Automatically Configured

- **Units**: Architectural with 1/16" precision
- **21 NCS-style layers** with correct colors, linetypes, and lineweights
- **Linetypes**: Hidden, Center, Phantom loaded
- **Text styles**: ANNO-TEXT, ANNO-TITLE
- **Dimension style**: ARCH-DIMS (architectural units, 1/16" precision)
- **Layout**: ARCH-D-Starter created
- **Cleanup**: Unwanted layers and content removed, drawing purged

### Requires Manual Configuration

- Annotation scales (SCALELISTEDIT)
- Page setup (printer/PDF device selection)
- Plot styles (CTB/STB assignment)
- Title block insertion (per office standard)

## Layer Structure

The template uses a simplified NCS/AIA layer naming convention:

```
A-WALL      Architectural walls
A-DOOR      Doors
A-WIND      Windows
A-FLOR      Floor patterns
A-CLNG      Ceiling (hidden linetype)
A-ROOF      Roof
A-STRS      Stairs
A-FURN      Furniture
A-GLAZ      Glazing
A-COLS      Architectural columns
A-HATCH     Hatch patterns
A-VIEW      Section/elevation marks
A-ANNO-*    Annotation layers (DIMS, TEXT, SYMB)
S-BEAM      Structural beams
S-COLS      Structural columns
C-GRID      Column grid
V-VPRT      Viewports (non-plotting)
```

See `LAYER_SCHEDULE.csv` for complete property assignments.

## Model Space Guidelines

- Draw all geometry at full scale (1:1) in model space
- Keep floor plans near the origin (0,0)
- For multi-story projects, separate floors vertically or use separate files with XREFs
- Use the correct layer for each element type

## Troubleshooting

### Script errors or stops

- Check the command line for error messages
- Some commands may prompt differently based on AutoCAD version
- See `ASSUMPTIONS_AND_LIMITATIONS.md` for known issues

### Layers not renamed

- Layers with objects on them cannot be renamed while those objects are selected
- Ensure nothing is selected before running the script

### Linetypes not loading

- The script attempts to load from `acad.lin`
- If your installation uses a different linetype file, load manually via LINETYPE command

## Standards Reference

This template is inspired by:
- U.S. National CAD Standard (NCS)
- AIA CAD Layer Guidelines
- Uniform Drawing System (UDS)

Simplified for residential architectural work while maintaining compatibility with full NCS workflows.
