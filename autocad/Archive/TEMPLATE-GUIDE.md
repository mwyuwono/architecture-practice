# AutoCAD DXF Template Creation Guide

Reference documentation for creating architectural DXF templates that open cleanly in AutoCAD (desktop and web).

## Quick Start

```bash
cd /path/to/autocad
source .venv/bin/activate
python3 generate_template.py
```

## DXF Format Requirements

### Version
Use **AC1032** (AutoCAD 2018) format. Earlier versions (AC1015/AutoCAD 2000) lack required structural elements for modern AutoCAD applications.

### Required Sections
A valid AC1032 DXF must include:
1. **HEADER** - System variables
2. **CLASSES** - Object class definitions
3. **TABLES** - VPORT, LTYPE, LAYER, STYLE, APPID, DIMSTYLE, BLOCK_RECORD
4. **BLOCKS** - `*Model_Space` and `*Paper_Space` definitions
5. **ENTITIES** - Drawing geometry
6. **OBJECTS** - Dictionaries and layouts
7. **EOF**

### Entity Structure
Every entity requires:
- Handle (code 5): Unique hex ID
- Owner (code 330): Parent handle
- Subclass markers (code 100): e.g., `AcDbEntity`, `AcDbLine`

**Recommended:** Use the `ezdxf` Python library to handle this complexity automatically.

---

## Units Configuration

| Variable | Value | Description |
|----------|-------|-------------|
| `$MEASUREMENT` | 0 | Imperial |
| `$INSUNITS` | 1 | Inches |
| `$LUNITS` | 4 | Architectural display |
| `$LUPREC` | 4 | Precision (4 decimal places) |
| `$TEXTSIZE` | 0.125 | Default text height (1/8") |
| `$DIMTXT` | 0.125 | Dimension text height |
| `$DIMASZ` | 0.125 | Arrow size |
| `$DIMSCALE` | 1.0 | Dimension scale |

---

## Sheet Sizes

| Size | Dimensions | Use Case |
|------|------------|----------|
| Arch A | 9" × 12" | Details, small plans |
| Arch B | 12" × 18" | Small residential |
| Arch C | 18" × 24" | Medium plans |
| **Arch D** | **24" × 36"** | Standard residential/commercial |
| Arch E | 36" × 48" | Large commercial |

### Sheet Geometry
- **Outer border**: Full sheet size (e.g., 36" × 24")
- **Inner margin**: 0.5" inset from border
- **Title block**: Lower-right corner, typically 14" × 7.5"

---

## Layer Standard (AIA/NCS)

### Naming Convention
`[Discipline]-[Major]-[Minor]`

| Prefix | Discipline |
|--------|------------|
| A- | Architecture |
| S- | Structural |
| M- | Mechanical |
| P- | Plumbing |
| E- | Electrical |
| FP- | Fire Protection |
| C- | Civil/Site |

### Lineweight Hierarchy

| Weight | mm | DXF Code 370 | Color | Use |
|--------|-----|--------------|-------|-----|
| Heavy | 0.60 | 60 | 1 (red) | Walls, columns, cut lines |
| Medium | 0.35 | 35 | 2 (yellow) | Doors, windows, fixtures |
| Light | 0.18 | 18 | 3 (green) | Glazing, ceiling, reinforcing |
| Very Light | 0.13 | 13 | 4 (cyan) | Furniture, hatching, topo |
| Text | 0.18 | 18 | 5 (blue) | Annotations, notes |
| Dimensions | 0.18 | 18 | 6 (magenta) | Dimension strings |
| Border | 0.35 | 35 | 7 (white) | Sheet border, title block |
| NoPlot | 0.00 | 0 | 8 (gray) | Viewports, DEFPOINTS |

### Complete Layer Inventory (53 Layers)

#### Utility / NoPlot
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| 0 | 7 | Continuous | 25 | Yes |
| DEFPOINTS | 8 | Continuous | 0 | No |
| A-NPLT-VIEWPORT | 8 | Continuous | 0 | No |
| A-REFR-XREF | 8 | Continuous | 0 | No |

#### Architecture
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| A-WALL | 1 | Continuous | 60 | Yes |
| A-WALL-OTLN | 1 | Continuous | 60 | Yes |
| A-DOOR | 2 | Continuous | 35 | Yes |
| A-WIND | 2 | Continuous | 35 | Yes |
| A-GLAZ | 3 | Continuous | 18 | Yes |
| A-ROOF | 2 | Continuous | 35 | Yes |
| A-FLOR | 2 | Continuous | 35 | Yes |
| A-CLNG | 3 | Continuous | 18 | Yes |
| A-STAIR | 2 | Continuous | 35 | Yes |
| A-CASE | 3 | Continuous | 18 | Yes |
| A-FIXT | 3 | Continuous | 18 | Yes |
| A-FURN | 4 | Continuous | 13 | Yes |
| A-EQPM | 4 | Continuous | 13 | Yes |
| A-HATCH | 4 | Continuous | 13 | Yes |
| A-OVERHD | 4 | HIDDEN | 13 | Yes |
| A-CNTR | 4 | CENTER | 13 | Yes |

#### Annotation / Sheet
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| A-ANNO-TEXT | 5 | Continuous | 18 | Yes |
| A-ANNO-DIMS | 6 | Continuous | 18 | Yes |
| A-ANNO-TAGS | 5 | Continuous | 18 | Yes |
| A-ANNO-KEYN | 5 | Continuous | 18 | Yes |
| A-ANNO-NOTE | 5 | Continuous | 18 | Yes |
| A-ANNO-GRID | 4 | CENTER | 13 | Yes |
| A-BORDER | 7 | Continuous | 35 | Yes |
| A-TTLB | 7 | Continuous | 18 | Yes |

#### Structure
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| S-COL | 1 | Continuous | 60 | Yes |
| S-BEAM | 1 | Continuous | 60 | Yes |
| S-SLAB | 2 | Continuous | 35 | Yes |
| S-FOUND | 1 | Continuous | 60 | Yes |
| S-REINF | 3 | Continuous | 18 | Yes |
| S-ANNO | 5 | Continuous | 18 | Yes |

#### Mechanical
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| M-SPLY | 2 | Continuous | 35 | Yes |
| M-RETN | 2 | Continuous | 35 | Yes |
| M-DIFF | 3 | Continuous | 18 | Yes |
| M-EQPM | 3 | Continuous | 18 | Yes |
| M-ANNO | 5 | Continuous | 18 | Yes |

#### Plumbing
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| P-PIPE | 2 | Continuous | 35 | Yes |
| P-FIXT | 3 | Continuous | 18 | Yes |
| P-ANNO | 5 | Continuous | 18 | Yes |

#### Electrical
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| E-POWR | 2 | Continuous | 35 | Yes |
| E-LITE | 3 | Continuous | 18 | Yes |
| E-LOWV | 3 | Continuous | 18 | Yes |
| E-ANNO | 5 | Continuous | 18 | Yes |

#### Fire Protection
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| FP-PIPE | 2 | Continuous | 35 | Yes |
| FP-HEAD | 3 | Continuous | 18 | Yes |
| FP-ANNO | 5 | Continuous | 18 | Yes |

#### Civil/Site
| Layer | Color | Linetype | LW | Plot |
|-------|-------|----------|-----|------|
| C-TOPO | 4 | Continuous | 13 | Yes |
| C-ROAD | 2 | Continuous | 35 | Yes |
| C-PLNT | 3 | Continuous | 18 | Yes |
| C-ANNO | 5 | Continuous | 18 | Yes |

---

## Linetypes

| Name | Pattern | Description |
|------|---------|-------------|
| Continuous | Solid | Default |
| DASHED | `__ __ __` | Hidden edges |
| CENTER | `____ _ ____` | Centerlines, grid |
| HIDDEN | `__ __ __` | Hidden/overhead |

---

## Python Generator Template

```python
import ezdxf
from ezdxf.enums import TextEntityAlignment

# Create AC1032 document
doc = ezdxf.new('R2018')

# Configure units
doc.header['$MEASUREMENT'] = 0  # Imperial
doc.header['$INSUNITS'] = 1     # Inches
doc.header['$LUNITS'] = 4       # Architectural
doc.header['$LUPREC'] = 4

# Add linetypes
doc.linetypes.add('DASHED', pattern=[0.5, -0.25])
doc.linetypes.add('CENTER', pattern=[1.25, -0.25, 0.25, -0.25])
doc.linetypes.add('HIDDEN', pattern=[0.25, -0.125])

# Add layer
doc.layers.add(
    name='A-WALL',
    color=1,                    # Red
    linetype='Continuous',
    lineweight=60,              # 0.60mm in hundredths
    plot=True
)

# Add geometry
msp = doc.modelspace()
msp.add_line((0, 0), (36, 0), dxfattribs={'layer': 'A-BORDER'})

# Save
doc.saveas('template.dxf')
```

---

## Verification Checklist

After generating a template:

- [ ] Opens in AutoCAD Web without "Design is empty" error
- [ ] Opens in AutoCAD for Mac without failure
- [ ] All layers visible in Layer Manager (53 total)
- [ ] Border geometry visible (36" × 24" for Arch D)
- [ ] Title block text readable
- [ ] Units display as Architectural (feet-inches)
- [ ] Linetypes available (Continuous, Dashed, Center, Hidden)

---

## Troubleshooting

### "Design is empty" error
- Missing `*Model_Space` / `*Paper_Space` blocks
- Missing entity handles or owner references
- Use AC1032 format, not AC1015

### File won't open at all
- Corrupted section structure
- Missing EOF marker
- Invalid group codes

### Layers missing
- Layer names case-sensitive
- Check LAYER table has correct count in code 70

---

## Files

| File | Purpose |
|------|---------|
| `generate_template.py` | Python script to generate DXF |
| `Architectural_Starter_ArchD_AIA_NCS.dxf` | Generated template |
| `example-dxf.dxf` | Reference working DXF (AC1032) |
| `.venv/` | Python virtual environment with ezdxf |
