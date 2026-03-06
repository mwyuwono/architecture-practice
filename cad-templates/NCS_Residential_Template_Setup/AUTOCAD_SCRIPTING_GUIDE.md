# AutoCAD Script (.scr) Reference Guide for Mac

A comprehensive guide to writing AutoCAD scripts, with emphasis on Mac-specific behavior and common pitfalls discovered through practical testing.

---

## Table of Contents

1. [Script File Basics](#script-file-basics)
2. [Critical Issue: Blank Lines](#critical-issue-blank-lines)
3. [Command Reference](#command-reference)
4. [Unavailable Commands on Mac](#unavailable-commands-on-mac)
5. [Dangerous Commands](#dangerous-commands)
6. [Mac-Specific Considerations](#mac-specific-considerations)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)
9. [Quick Reference Card](#quick-reference-card)

---

## Script File Basics

### What is a .scr File?

A script file (`.scr`) is a plain text file containing AutoCAD commands that execute sequentially, as if typed at the command line. Scripts automate repetitive tasks like setting up templates, layer structures, and drawing configurations.

### File Format Requirements

| Property | Requirement |
|----------|-------------|
| Extension | `.scr` |
| Encoding | ASCII or UTF-8 (without BOM) |
| Line endings | Unix (LF) or Windows (CRLF) both work |
| Editor | Any plain text editor (VS Code, TextEdit in plain text mode) |

### Running a Script

1. Open AutoCAD with your target drawing
2. Type `SCRIPT` at the command line
3. Navigate to and select your `.scr` file
4. Watch the command line for any errors

### Comment Syntax

```
; This is a comment - AutoCAD ignores lines starting with semicolon
; Comments help document what each section does
```

### How AutoCAD Processes Scripts

AutoCAD reads the script file line by line and:
1. Sends each line to the command processor
2. Treats spaces as parameter separators
3. Treats blank lines as **Enter key presses**
4. Continues until end of file or error

---

## Critical Issue: Blank Lines

### The Problem

**Blank lines in script files act as Enter key presses.**

This seems harmless, but at the `Command:` prompt, pressing Enter **repeats the previous command**. This causes scripts to behave unpredictably.

### Example of the Problem

```
; BAD - This will cause issues
-LAYER N A-WALL C 1 A-WALL

-LAYER N A-DOOR C 30 A-DOOR

```

What happens:
1. First `-LAYER` command runs correctly
2. Blank line sends Enter → exits LAYER command
3. Second blank line sends Enter at `Command:` prompt → **repeats `-LAYER` again unexpectedly**

### The Solution

Remove unnecessary blank lines. Keep comments adjacent to commands:

```
; GOOD - No extra blank lines
-LAYER N A-WALL C 1 A-WALL LT Continuous A-WALL LW 0.50 A-WALL

-LAYER N A-DOOR C 30 A-DOOR LT Continuous A-DOOR LW 0.35 A-DOOR

```

### When Blank Lines ARE Needed

Some commands require a blank line to confirm/exit:

| Command | Needs Blank Line After? | Reason |
|---------|------------------------|--------|
| `-LAYER` | Yes (one) | Exits the LAYER command |
| `-LINETYPE L` | Yes (one) | Confirms linetype load |
| `-STYLE` | No | Completes automatically |
| `SETVAR` | No | Single-line command |
| `-DIMSTYLE` | No | Completes automatically |

---

## Command Reference

### -UNITS Command

Sets drawing units and precision.

**Syntax:**
```
-UNITS [linear_type] [denominator] [angular_type] [angular_precision]
```

**Parameters:**

| Parameter | Values | Notes |
|-----------|--------|-------|
| linear_type | 1=Scientific, 2=Decimal, 3=Engineering, **4=Architectural**, 5=Fractional | Use 4 for feet-inches |
| denominator | 1, 2, 4, 8, **16**, 32, 64, 128, 256 | Smallest displayable fraction |
| angular_type | **1=Decimal Degrees**, 2=Deg/Min/Sec, 3=Grads, 4=Radians, 5=Surveyor | Must be 1-5, NOT 0 |
| angular_precision | 0-8 | Decimal places for angles |

**Correct Example:**
```
; Set Architectural units with 1/16" precision
-UNITS 4 16 1 0
```

**Common Mistakes:**
- Using `5` instead of `16` for denominator (5 is not a valid denominator)
- Using `0` for angular type (must be 1-5)

---

### -LAYER Command

Creates and modifies layers.

**Syntax for creating a new layer with properties:**
```
-LAYER N [name] C [color] [name] LT [linetype] [name] LW [lineweight] [name]

```
Note: Requires one blank line after to exit LAYER command.

**Parameter Reference:**

| Code | Meaning | Example |
|------|---------|---------|
| N | New layer | `N A-WALL` |
| C | Color | `C 1 A-WALL` (color 1 = red) |
| LT | Linetype | `LT Continuous A-WALL` |
| LW | Lineweight | `LW 0.50 A-WALL` (in mm) |
| P | Plot setting | `P N A-WALL` (No plot) |
| S | Set current | `S 0` |

**Setting Non-Plotting Layer:**
```
-LAYER N V-VPRT C 8 V-VPRT LT Continuous V-VPRT P N V-VPRT

```
Note: `P N V-VPRT` = Plot preference (N=No), then layer name. Order matters!

**Common Colors:**

| Number | Color |
|--------|-------|
| 1 | Red |
| 2 | Yellow |
| 3 | Green |
| 4 | Cyan |
| 5 | Blue |
| 6 | Magenta |
| 7 | White/Black |
| 8 | Dark Gray |
| 9 | Light Gray |
| 10 | Red (variant) |
| 30 | Orange |
| 40 | Yellow-Orange |
| 252 | Light Gray |

**Common Lineweights (mm):**
- 0.09 - Hairline (hatches)
- 0.18 - Light (annotations, furniture)
- 0.25 - Medium-light (glazing)
- 0.35 - Medium (doors, windows)
- 0.50 - Heavy (walls, columns)

---

### -LINETYPE Command

Loads linetypes from definition files.

**Syntax:**
```
-LINETYPE L [linetype_name] [file.lin]

```
Note: Requires blank line after to confirm.

**Example:**
```
; Load standard linetypes
-LINETYPE L Hidden acad.lin

-LINETYPE L Center acad.lin

-LINETYPE L Phantom acad.lin

```

**Standard Linetypes in acad.lin:**
- Continuous (built-in)
- Hidden
- Center
- Phantom
- Dashed
- Dashdot
- Border
- Divide

---

### -STYLE Command

Creates text styles.

**Syntax:**
```
-STYLE [name] [font] [height] [width_factor] [oblique_angle] [backwards] [upside_down]
```

**Parameters:**

| Parameter | Type | Notes |
|-----------|------|-------|
| name | String | Style name |
| font | String | Font name (e.g., Arial) |
| height | Number | 0 = variable height |
| width_factor | Number | 1 = normal |
| oblique_angle | Number | 0 = no slant |
| backwards | Y/N | N = normal |
| upside_down | Y/N | N = normal |

**Correct Example:**
```
-STYLE ANNO-TEXT Arial 0 1 0 N N
-STYLE ANNO-TITLE Arial 0 1 0 N N
```

**Common Mistake:**
```
; WRONG - Too many N's
-STYLE ANNO-TEXT Arial 0 1 0 N N N
```

---

### SETVAR Command

Sets system variables.

**Syntax:**
```
SETVAR [variable_name] [value]
```

This is a single-line command - no blank line needed after.

**Example:**
```
SETVAR LWDISPLAY 1
SETVAR INSUNITS 1
```

**Important System Variables:**

| Variable | Values | Description |
|----------|--------|-------------|
| LWDISPLAY | 0/1 | Lineweight display on/off |
| INSUNITS | 1=Inches, 4=mm | Insertion units |

---

### Dimension Variables (DIMVAR)

Set dimension properties before saving a dimension style.

**Key Dimension Variables:**

| Variable | Description | Typical Value |
|----------|-------------|---------------|
| DIMLUNIT | Linear unit format | 4 (Architectural) |
| DIMASZ | Arrow size | 0.125 (1/8") |
| DIMTXT | Text height | 0.09375 (3/32") |
| DIMEXO | Extension line offset | 0.0625 (1/16") |
| DIMEXE | Extension beyond dim | 0.125 (1/8") |
| DIMDLI | Baseline spacing | 0.375 (3/8") |
| DIMGAP | Text gap | 0.0625 (1/16") |
| DIMTAD | Text above dim line | 1 (on) |
| DIMTIH | Text inside horizontal | 0 (off) |
| DIMTOH | Text outside horizontal | 0 (off) |
| DIMZIN | Zero suppression | 0 (show all) |
| DIMFRAC | Fraction format | 2 (diagonal) |

**Example:**
```
; Set dimension variables
SETVAR DIMLUNIT 4
SETVAR DIMASZ 0.125
SETVAR DIMTXT 0.09375
SETVAR DIMEXO 0.0625
SETVAR DIMEXE 0.125
SETVAR DIMDLI 0.375
SETVAR DIMGAP 0.0625
SETVAR DIMTAD 1
SETVAR DIMTIH 0
SETVAR DIMTOH 0
SETVAR DIMZIN 0
SETVAR DIMFRAC 2
```

---

### -DIMSTYLE Command

Saves and restores dimension styles.

**Save current settings as a named style:**
```
-DIMSTYLE S [style_name]
```

**Restore (make current) a named style:**
```
-DIMSTYLE R [style_name]
```

**Complete Workflow:**
```
; First set all DIMVAR values
SETVAR DIMLUNIT 4
SETVAR DIMASZ 0.125
; ... more settings ...

; Then save as named style
-DIMSTYLE S ARCH-DIMS

; Make it current
-DIMSTYLE R ARCH-DIMS
```

---

### -LAYOUT Command

Creates paper space layouts.

**Syntax:**
```
-LAYOUT N [layout_name]
```

**Example:**
```
-LAYOUT N ARCH-D-Starter
```

---

## Unavailable Commands on Mac

Some commands available on Windows AutoCAD are not available on Mac versions.

| Command | Status on Mac | Workaround |
|---------|---------------|------------|
| `-LAYDEL` | Not available (AutoCAD 2018 Mac) | Delete manually via Layer Properties Manager |
| `LAYMRG` | May vary by version | Manual layer merge |
| Some Express Tools | Limited availability | Use standard commands |

**When a command isn't available:**
1. Script will show "Unknown command" error
2. Script may continue or stop depending on subsequent lines
3. Document the manual step in your checklist

---

## Dangerous Commands

### -PURGE Command

**The Problem:**
```
-PURGE A

```

`PURGE` deletes "unused" items from the drawing, including:
- Layers with no objects
- Unused linetypes
- Unused text styles
- Unused dimension styles

**Why It's Dangerous in Scripts:**

If you create layers via script but haven't drawn anything on them yet, PURGE considers them "unused" and **deletes them all**.

**Example Disaster:**
```
; Create 20 layers...
-LAYER N A-WALL C 1 A-WALL ...
-LAYER N A-DOOR C 30 A-DOOR ...
; ... 18 more layers ...

; Oops - this deletes everything we just created!
-PURGE A
Y
```

**Rule:** Never use PURGE in a template setup script. Only purge after objects exist on layers.

---

## Mac-Specific Considerations

### What Works the Same

| Feature | Mac Status |
|---------|------------|
| Script file execution | Same as Windows |
| Command syntax | Generally identical |
| DXF file format | Fully compatible |
| Basic commands | All work |

### What May Differ

| Item | Notes |
|------|-------|
| Command prompts | May have slight wording differences |
| File paths | Use Mac path format in scripts |
| Font availability | Arial, Arial Black standard on macOS |
| Linetype file location | `acad.lin` at default install location |
| Some Express Tools | Limited availability |
| Certain specialized commands | Test before deploying |

### Recommended Mac Fonts

If specified fonts aren't available:

| Preferred | Fallback |
|-----------|----------|
| Arial | Helvetica |
| Arial Black | Helvetica Neue Bold |
| Arial Narrow | Helvetica Neue Condensed |

---

## Best Practices

### 1. Start Simple

Begin with a minimal base drawing:
- Few existing layers (just 0 and Defpoints)
- No complex existing configurations
- Clean slate is easier than modifying

### 2. Test Incrementally

Don't write 100-line scripts and run them blind:
1. Write 5-10 lines
2. Run and verify
3. Add more lines
4. Repeat

### 3. Watch the Command Line

During script execution:
- Keep command line visible
- Watch for error messages
- Note any unexpected prompts
- Stop if things go wrong (ESC key)

### 4. Structure Your Script

```
; ============================================
; SECTION 1: UNITS AND SYSTEM VARIABLES
; ============================================
-UNITS 4 16 1 0
SETVAR LWDISPLAY 1

; ============================================
; SECTION 2: LINETYPES
; ============================================
-LINETYPE L Hidden acad.lin

; ============================================
; SECTION 3: LAYERS
; ============================================
-LAYER N A-WALL C 1 A-WALL LT Continuous A-WALL LW 0.50 A-WALL

; ... etc
```

### 5. Avoid Blank Line Traps

- Never have consecutive blank lines
- Put comments immediately before commands
- One blank line only where required (after LAYER, LINETYPE)

### 6. Document Manual Steps

Some things can't be scripted. Always include a manual checklist:
- Annotation scales (SCALELISTEDIT)
- Page setup (machine-dependent)
- Plot style tables (path-dependent)
- Title blocks (office-specific)

### 7. Version Your Scripts

Track changes to scripts:
- Use git or similar version control
- Comment changes with dates
- Keep working versions separate from experiments

---

## Troubleshooting

### Script Stops Unexpectedly

**Possible Causes:**
1. Unknown command (check Mac availability)
2. Wrong number of parameters
3. Unexpected prompt requiring input
4. Command waiting for object selection

**Solutions:**
1. Check command line for error message
2. Verify command syntax in AutoCAD documentation
3. Test command manually before scripting
4. Add missing parameters or responses

### Commands Repeat Unexpectedly

**Cause:** Blank lines at `Command:` prompt repeat previous command.

**Solution:** Remove extra blank lines from script.

### Layers/Styles Not Created

**Possible Causes:**
1. PURGE deleted them (if run after creation)
2. Command syntax error (silent failure)
3. Name already exists (may skip creation)

**Solutions:**
1. Remove PURGE from script
2. Verify syntax against documentation
3. Use unique names or delete existing first

### Wrong Properties Applied

**Possible Causes:**
1. Parameters in wrong order
2. Missing layer name repetition
3. Incorrect value format

**Solution:** Check -LAYER syntax - layer name must be repeated after each property code:
```
; WRONG
-LAYER N A-WALL C 1 LT Continuous LW 0.50

; CORRECT
-LAYER N A-WALL C 1 A-WALL LT Continuous A-WALL LW 0.50 A-WALL
```

---

## Quick Reference Card

### Units
```
-UNITS 4 16 1 0                    ; Architectural, 1/16", Decimal Degrees
```

### Layer (with all properties)
```
-LAYER N NAME C [color] NAME LT [linetype] NAME LW [lw] NAME

```

### Layer (non-plotting)
```
-LAYER N NAME C [color] NAME LT [linetype] NAME P N NAME

```

### Linetype
```
-LINETYPE L [name] acad.lin

```

### Text Style
```
-STYLE NAME Arial 0 1 0 N N
```

### Dimension Style
```
SETVAR DIMLUNIT 4
; ... other DIMVAR settings ...
-DIMSTYLE S STYLENAME
-DIMSTYLE R STYLENAME
```

### Layout
```
-LAYOUT N LayoutName
```

### System Variables
```
SETVAR LWDISPLAY 1
SETVAR INSUNITS 1
```

### Final Commands
```
REGEN
ZOOM E
```

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2024-XX-XX | 1.0 | Initial version based on NCS Residential Template setup |

---

## Related Files

- [SETUP_SCRIPT.scr](SETUP_SCRIPT.scr) - Working example script
- [MANUAL_ACTIONS_CHECKLIST.md](MANUAL_ACTIONS_CHECKLIST.md) - Steps requiring manual work
- [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) - QA verification
- [TEMPLATE_SPEC.md](TEMPLATE_SPEC.md) - Target configuration specification
- [ASSUMPTIONS_AND_LIMITATIONS.md](ASSUMPTIONS_AND_LIMITATIONS.md) - Platform notes
