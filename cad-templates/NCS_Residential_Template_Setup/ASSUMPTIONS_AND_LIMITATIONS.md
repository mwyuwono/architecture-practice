# Assumptions and Limitations

This document describes what was assumed about AutoCAD for Mac capabilities, what could not be confirmed, and what should be tested before office-wide adoption.

## Platform Assumptions

### AutoCAD for Mac Version

- **Assumed:** AutoCAD 2020 for Mac or later
- **Reason:** Script commands and prompts may vary between versions
- **Risk:** Older versions may have different command sequences

### Script Execution

- **Assumed:** SCR files execute the same way on Mac as Windows
- **Verified:** Basic SCR execution is supported on AutoCAD for Mac
- **Risk:** Some command prompts may differ slightly; watch command line during execution

### Linetype Files

- **Assumed:** `acad.lin` linetype definition file is available at default location
- **Risk:** Custom AutoCAD installations may use different paths
- **Mitigation:** If linetypes don't load, use LINETYPE command to load manually from your installation's linetype file

### Font Availability

- **Assumed:** Arial and Arial Black fonts are installed (standard macOS fonts)
- **Risk:** Custom Mac configurations may not have these fonts
- **Mitigation:** Script specifies fallback fonts; if neither works, substitute Helvetica

## Automation Limitations

### What Could NOT Be Automated

| Item | Reason | Manual Step Required |
|------|--------|---------------------|
| Annotation scales | SCALELISTEDIT not reliably scriptable | Add scales manually |
| Page setup | Machine-dependent (printers, paths) | Configure in Page Setup Manager |
| Plot style tables | File paths not portable | Assign CTB/STB manually |
| Sheet Set Manager | No scripting API on Mac | Create sheet sets manually if needed |
| Title block | Office-specific design | Insert manually |
| PDF printer selection | Machine-specific | Select in Page Setup |

### What Was Partially Automated

| Item | Automated Part | Manual Verification |
|------|----------------|---------------------|
| Dimension style | DIMVAR settings + save | Verify settings took effect |
| Text styles | Style creation + font | Verify fonts resolved |
| Linetypes | Load command | Verify loaded in LINETYPE list |
| Layouts | Layout creation | Configure page setup |

### What Was Fully Automated

| Item | Notes |
|------|-------|
| Layer creation | All 21 layers with properties |
| Layer renaming | Existing layers renamed to NCS |
| Layer deletion | Unwanted layers removed |
| Entity deletion | Title Block content deleted |
| Unit settings | Architectural, 1/16" |
| System variables | LWDISPLAY, INSUNITS |
| Purge | Unused items removed |

## Known Issues and Workarounds

### Issue 1: LAYDEL Command Variation

The LAYDEL command may prompt differently in some AutoCAD versions.

**Symptoms:**
- Script stops at "Select object on layer to delete"
- Or prompts for confirmation unexpectedly

**Workaround:**
- If script fails at this point, manually delete Title Block layer:
  1. Select all objects on Title Block layer (QSELECT)
  2. Delete them (ERASE)
  3. Delete the layer (-LAYER > D > Title Block)

### Issue 2: Layer Property Assignment

The -LAYER command syntax for setting multiple properties in one call can be version-sensitive.

**Symptoms:**
- Some layer properties not applied
- Script continues but layers have wrong settings

**Workaround:**
- Open Layer Properties Manager
- Manually correct any incorrect properties
- Use LAYER_SCHEDULE.csv as reference

### Issue 3: Dimension Style Complexity

Dimension styles have many variables, and DIMSTYLE scripting is notoriously fragile.

**Symptoms:**
- ARCH-DIMS created but settings incorrect
- Or style not set as current

**Workaround:**
- Manually modify ARCH-DIMS via DIMSTYLE dialog
- Reference TEMPLATE_SPEC.md for correct values

### Issue 4: Font Substitution

If specified fonts aren't available, AutoCAD may substitute or prompt.

**Symptoms:**
- Font substitution dialog appears during script
- Text styles show different fonts than expected

**Workaround:**
- Accept substitution or
- After script, modify text styles to use available fonts
- Recommended Mac alternatives: Helvetica, Helvetica Neue

## Testing Recommendations

### Before Office Adoption

1. **Test on target AutoCAD version**
   - Run script on the exact version used in your office
   - Note any prompt differences
   - Document modifications needed

2. **Test plotting workflow**
   - Configure page setup with your actual plotter/PDF driver
   - Print a test sheet
   - Verify lineweights print correctly
   - Verify non-plot layers don't appear

3. **Test with sample project**
   - Create a simple floor plan using the template
   - Add dimensions, text, hatches
   - Verify layers work as expected
   - Verify scale list covers your needs

4. **Test XREF workflow**
   - Create a model file from template
   - XREF it into a sheet file
   - Verify layer behavior in XREF context

### Recommended Modifications

Based on your testing, you may want to:

| Modification | When Needed |
|--------------|-------------|
| Add more layers | If your workflow needs MEP, landscape, etc. |
| Modify lineweights | If your plotter produces different results |
| Add annotation scales | If you use scales not in the list |
| Change default colors | If your office uses different color standards |
| Add dimension style variants | If you need interior vs site dimensions |

## Version Compatibility Notes

### AutoCAD 2020-2024 for Mac

- Script should work without modification
- LAYDEL command available
- -LAYER command syntax stable

### AutoCAD 2019 and Earlier

- Not tested
- Some commands may have different syntax
- DIMVAR names should be stable

### AutoCAD LT for Mac

- Scripts (.scr) supported
- Some commands may be limited or unavailable
- Test thoroughly before adoption

## Future Enhancements

If fuller automation becomes possible:

1. **AutoLISP routines**
   - Create .lsp file for complex operations
   - Note: AutoLISP support on Mac is limited compared to Windows

2. **CUI/CUIX customization**
   - Custom ribbon panels for layer switching
   - Requires separate customization file

3. **Dynamic blocks**
   - Door, window, and fixture blocks with parameters
   - Would need separate block library

4. **Sheet Set template**
   - DST file for Sheet Set Manager
   - Requires manual setup per project

5. **Python scripting**
   - Modern AutoCAD versions support Python
   - Could enable more sophisticated automation

## Support and Updates

This template package is provided as-is. When updating:

1. Document what changed between versions
2. Test changes on a non-production drawing first
3. Keep a backup of working template before modifications
4. Update this document with any new assumptions or limitations discovered
