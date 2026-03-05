#!/usr/bin/env python3
"""
Generate Architectural_Starter_ArchD_AIA_NCS.dxf
AC1032 format with AIA/NCS layer standard and Arch D sheet setup.
"""

import ezdxf
from ezdxf.enums import TextEntityAlignment

# Layer definitions from template-reqs.md
# Format: (name, color, linetype, lineweight_mm, plot)
# Colors: heavy=1, medium=2, light=3, very light=4, text=5, dims=6, border=7, noplot=8
# Lineweights in mm: heavy=0.60, medium=0.35, light=0.18, very light=0.13

LAYERS = [
    # Utility / NoPlot
    ("0", 7, "Continuous", 0.25, True),
    ("DEFPOINTS", 8, "Continuous", 0.00, False),
    ("A-NPLT-VIEWPORT", 8, "Continuous", 0.00, False),
    ("A-REFR-XREF", 8, "Continuous", 0.00, False),

    # Architecture - Heavy
    ("A-WALL", 1, "Continuous", 0.60, True),
    ("A-WALL-OTLN", 1, "Continuous", 0.60, True),

    # Architecture - Medium
    ("A-DOOR", 2, "Continuous", 0.35, True),
    ("A-WIND", 2, "Continuous", 0.35, True),
    ("A-ROOF", 2, "Continuous", 0.35, True),
    ("A-FLOR", 2, "Continuous", 0.35, True),
    ("A-STAIR", 2, "Continuous", 0.35, True),

    # Architecture - Light
    ("A-GLAZ", 3, "Continuous", 0.18, True),
    ("A-CLNG", 3, "Continuous", 0.18, True),
    ("A-CASE", 3, "Continuous", 0.18, True),
    ("A-FIXT", 3, "Continuous", 0.18, True),

    # Architecture - Very Light
    ("A-FURN", 4, "Continuous", 0.13, True),
    ("A-EQPM", 4, "Continuous", 0.13, True),
    ("A-HATCH", 4, "Continuous", 0.13, True),
    ("A-OVERHD", 4, "HIDDEN", 0.13, True),
    ("A-CNTR", 4, "CENTER", 0.13, True),

    # Annotation / Sheet
    ("A-ANNO-TEXT", 5, "Continuous", 0.18, True),
    ("A-ANNO-DIMS", 6, "Continuous", 0.18, True),
    ("A-ANNO-TAGS", 5, "Continuous", 0.18, True),
    ("A-ANNO-KEYN", 5, "Continuous", 0.18, True),
    ("A-ANNO-NOTE", 5, "Continuous", 0.18, True),
    ("A-ANNO-GRID", 4, "CENTER", 0.13, True),
    ("A-BORDER", 7, "Continuous", 0.35, True),
    ("A-TTLB", 7, "Continuous", 0.18, True),

    # Structure
    ("S-COL", 1, "Continuous", 0.60, True),
    ("S-BEAM", 1, "Continuous", 0.60, True),
    ("S-SLAB", 2, "Continuous", 0.35, True),
    ("S-FOUND", 1, "Continuous", 0.60, True),
    ("S-REINF", 3, "Continuous", 0.18, True),
    ("S-ANNO", 5, "Continuous", 0.18, True),

    # Mechanical
    ("M-SPLY", 2, "Continuous", 0.35, True),
    ("M-RETN", 2, "Continuous", 0.35, True),
    ("M-DIFF", 3, "Continuous", 0.18, True),
    ("M-EQPM", 3, "Continuous", 0.18, True),
    ("M-ANNO", 5, "Continuous", 0.18, True),

    # Plumbing
    ("P-PIPE", 2, "Continuous", 0.35, True),
    ("P-FIXT", 3, "Continuous", 0.18, True),
    ("P-ANNO", 5, "Continuous", 0.18, True),

    # Electrical
    ("E-POWR", 2, "Continuous", 0.35, True),
    ("E-LITE", 3, "Continuous", 0.18, True),
    ("E-LOWV", 3, "Continuous", 0.18, True),
    ("E-ANNO", 5, "Continuous", 0.18, True),

    # Fire Protection
    ("FP-PIPE", 2, "Continuous", 0.35, True),
    ("FP-HEAD", 3, "Continuous", 0.18, True),
    ("FP-ANNO", 5, "Continuous", 0.18, True),

    # Site/Civil
    ("C-TOPO", 4, "Continuous", 0.13, True),
    ("C-ROAD", 2, "Continuous", 0.35, True),
    ("C-PLNT", 3, "Continuous", 0.18, True),
    ("C-ANNO", 5, "Continuous", 0.18, True),
]


def create_template():
    # Create new DXF document with AC1032 (AutoCAD 2018)
    doc = ezdxf.new('R2018')

    # Configure units: Imperial (inches), Architectural display
    doc.header['$MEASUREMENT'] = 0  # Imperial
    doc.header['$INSUNITS'] = 1     # Inches
    doc.header['$LUNITS'] = 4       # Architectural
    doc.header['$LUPREC'] = 4       # Precision
    doc.header['$TEXTSIZE'] = 0.125
    doc.header['$DIMTXT'] = 0.125
    doc.header['$DIMASZ'] = 0.125
    doc.header['$DIMSCALE'] = 1.0

    # Set drawing extents for Arch D (36" x 24")
    doc.header['$LIMMIN'] = (0, 0)
    doc.header['$LIMMAX'] = (36, 24)
    doc.header['$EXTMIN'] = (0, 0, 0)
    doc.header['$EXTMAX'] = (36, 24, 0)

    # Add linetypes if not present
    if 'DASHED' not in doc.linetypes:
        doc.linetypes.add('DASHED', pattern=[0.5, -0.25], description='Dashed __ __ __')
    if 'CENTER' not in doc.linetypes:
        doc.linetypes.add('CENTER', pattern=[1.25, -0.25, 0.25, -0.25], description='Center ____ _ ____ _')
    if 'HIDDEN' not in doc.linetypes:
        doc.linetypes.add('HIDDEN', pattern=[0.25, -0.125], description='Hidden __ __ __')

    # Add layers
    for name, color, linetype, lineweight, plot in LAYERS:
        if name in doc.layers:
            # Layer already exists, just configure it
            layer = doc.layers.get(name)
            layer.color = color
            layer.linetype = linetype
            layer.dxf.lineweight = int(lineweight * 100)  # Convert mm to 1/100 mm
            layer.dxf.plot = 1 if plot else 0
        else:
            doc.layers.add(
                name=name,
                color=color,
                linetype=linetype,
                lineweight=int(lineweight * 100),  # Convert mm to 1/100 mm
                plot=plot
            )

    # Get modelspace
    msp = doc.modelspace()

    # Draw outer border (36" x 24") on A-BORDER
    msp.add_line((0, 0), (36, 0), dxfattribs={'layer': 'A-BORDER'})
    msp.add_line((36, 0), (36, 24), dxfattribs={'layer': 'A-BORDER'})
    msp.add_line((36, 24), (0, 24), dxfattribs={'layer': 'A-BORDER'})
    msp.add_line((0, 24), (0, 0), dxfattribs={'layer': 'A-BORDER'})

    # Draw inner margin (0.5" offset) on A-BORDER
    msp.add_line((0.5, 0.5), (35.5, 0.5), dxfattribs={'layer': 'A-BORDER'})
    msp.add_line((35.5, 0.5), (35.5, 23.5), dxfattribs={'layer': 'A-BORDER'})
    msp.add_line((35.5, 23.5), (0.5, 23.5), dxfattribs={'layer': 'A-BORDER'})
    msp.add_line((0.5, 23.5), (0.5, 0.5), dxfattribs={'layer': 'A-BORDER'})

    # Title block zone in lower right (approx 14" wide x 7.5" high)
    # Position: right edge at x=35.5, bottom at y=0.5
    tb_left = 35.5 - 14  # 21.5
    tb_bottom = 0.5
    tb_right = 35.5
    tb_top = 0.5 + 7.5  # 8.0

    # Title block outer box
    msp.add_line((tb_left, tb_bottom), (tb_right, tb_bottom), dxfattribs={'layer': 'A-TTLB'})
    msp.add_line((tb_left, tb_top), (tb_right, tb_top), dxfattribs={'layer': 'A-TTLB'})
    msp.add_line((tb_left, tb_bottom), (tb_left, tb_top), dxfattribs={'layer': 'A-TTLB'})

    # Horizontal dividers in title block
    msp.add_line((tb_left, tb_bottom + 1.5), (tb_right, tb_bottom + 1.5), dxfattribs={'layer': 'A-TTLB'})
    msp.add_line((tb_left, tb_bottom + 3.0), (tb_right, tb_bottom + 3.0), dxfattribs={'layer': 'A-TTLB'})
    msp.add_line((tb_left, tb_bottom + 5.0), (tb_right, tb_bottom + 5.0), dxfattribs={'layer': 'A-TTLB'})

    # Vertical divider for scale/date/sheet section
    msp.add_line((tb_left + 7, tb_bottom), (tb_left + 7, tb_bottom + 3.0), dxfattribs={'layer': 'A-TTLB'})

    # Placeholder text labels (text height 0.125")
    text_height = 0.125

    # PROJECT label
    msp.add_text(
        'PROJECT',
        dxfattribs={
            'layer': 'A-TTLB',
            'height': text_height,
            'style': 'Standard'
        }
    ).set_placement((tb_left + 0.25, tb_top - 0.5), align=TextEntityAlignment.LEFT)

    # DRAWING TITLE label
    msp.add_text(
        'DRAWING TITLE',
        dxfattribs={
            'layer': 'A-TTLB',
            'height': text_height,
            'style': 'Standard'
        }
    ).set_placement((tb_left + 0.25, tb_bottom + 3.5), align=TextEntityAlignment.LEFT)

    # SHEET label
    msp.add_text(
        'SHEET',
        dxfattribs={
            'layer': 'A-TTLB',
            'height': text_height,
            'style': 'Standard'
        }
    ).set_placement((tb_left + 7.25, tb_bottom + 2.25), align=TextEntityAlignment.LEFT)

    # DATE label
    msp.add_text(
        'DATE',
        dxfattribs={
            'layer': 'A-TTLB',
            'height': text_height,
            'style': 'Standard'
        }
    ).set_placement((tb_left + 7.25, tb_bottom + 0.75), align=TextEntityAlignment.LEFT)

    # SCALE label
    msp.add_text(
        'SCALE',
        dxfattribs={
            'layer': 'A-TTLB',
            'height': text_height,
            'style': 'Standard'
        }
    ).set_placement((tb_left + 0.25, tb_bottom + 0.75), align=TextEntityAlignment.LEFT)

    return doc


def main():
    import os

    # Generate the template
    doc = create_template()

    # Save to file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'Architectural_Starter_ArchD_AIA_NCS.dxf')

    doc.saveas(output_path)
    print(f"Created: {output_path}")

    # Verify
    print(f"\nVerification:")
    print(f"  Layers: {len(doc.layers)} defined")
    print(f"  Entities in modelspace: {len(list(doc.modelspace()))}")
    print(f"  DXF version: {doc.dxfversion}")


if __name__ == '__main__':
    main()
