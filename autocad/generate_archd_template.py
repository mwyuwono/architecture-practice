#!/usr/bin/env python3
"""Generate an AutoCAD-friendly Arch D starter DXF template."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf.lldxf.const import DXFKeyError

OUTPUT_FILENAME = "Architectural_Starter_ArchD_AIA_NCS.dxf"

TEXT_STYLE_STD = "A-TEXT-STD"
TEXT_STYLE_ANNO = "A-TEXT-ANNO"
DIM_STYLE_STD = "A-DIM-STD"
DIM_STYLE_ANNO = "A-DIM-ANNO"
ANNO_SCALE = '1/4"=1\'-0"'

# (name, color, linetype, lineweight_mm, plot)
LAYERS = [
    ("0", 7, "Continuous", 0.35, True),
    ("DEFPOINTS", 8, "Continuous", 0.00, False),
    ("A-NPLT-VIEWPORT", 8, "Continuous", 0.00, False),
    ("A-REFR-XREF", 8, "Continuous", 0.00, False),
    ("A-WALL", 1, "Continuous", 0.60, True),
    ("A-WALL-OTLN", 1, "Continuous", 0.60, True),
    ("A-DOOR", 2, "Continuous", 0.35, True),
    ("A-WIND", 2, "Continuous", 0.35, True),
    ("A-GLAZ", 3, "Continuous", 0.18, True),
    ("A-ROOF", 2, "Continuous", 0.35, True),
    ("A-FLOR", 2, "Continuous", 0.35, True),
    ("A-CLNG", 3, "Continuous", 0.18, True),
    ("A-STAIR", 2, "Continuous", 0.35, True),
    ("A-CASE", 3, "Continuous", 0.18, True),
    ("A-FIXT", 3, "Continuous", 0.18, True),
    ("A-FURN", 4, "Continuous", 0.13, True),
    ("A-EQPM", 4, "Continuous", 0.13, True),
    ("A-HATCH", 4, "Continuous", 0.13, True),
    ("A-OVERHD", 4, "HIDDEN", 0.13, True),
    ("A-CNTR", 4, "CENTER", 0.13, True),
    ("A-ANNO-TEXT", 5, "Continuous", 0.18, True),
    ("A-ANNO-DIMS", 6, "Continuous", 0.18, True),
    ("A-ANNO-TAGS", 5, "Continuous", 0.18, True),
    ("A-ANNO-KEYN", 5, "Continuous", 0.18, True),
    ("A-ANNO-NOTE", 5, "Continuous", 0.18, True),
    ("A-ANNO-GRID", 4, "CENTER", 0.13, True),
    ("A-BORDER", 7, "Continuous", 0.35, True),
    ("A-TTLB", 7, "Continuous", 0.18, True),
    ("S-COL", 1, "Continuous", 0.60, True),
    ("S-BEAM", 1, "Continuous", 0.60, True),
    ("S-SLAB", 2, "Continuous", 0.35, True),
    ("S-FOUND", 1, "Continuous", 0.60, True),
    ("S-REINF", 3, "Continuous", 0.18, True),
    ("S-ANNO", 5, "Continuous", 0.18, True),
    ("M-SPLY", 2, "Continuous", 0.35, True),
    ("M-RETN", 2, "Continuous", 0.35, True),
    ("M-DIFF", 3, "Continuous", 0.18, True),
    ("M-EQPM", 3, "Continuous", 0.18, True),
    ("M-ANNO", 5, "Continuous", 0.18, True),
    ("P-PIPE", 2, "Continuous", 0.35, True),
    ("P-FIXT", 3, "Continuous", 0.18, True),
    ("P-ANNO", 5, "Continuous", 0.18, True),
    ("E-POWR", 2, "Continuous", 0.35, True),
    ("E-LITE", 3, "Continuous", 0.18, True),
    ("E-LOWV", 3, "Continuous", 0.18, True),
    ("E-ANNO", 5, "Continuous", 0.18, True),
    ("FP-PIPE", 2, "Continuous", 0.35, True),
    ("FP-HEAD", 3, "Continuous", 0.18, True),
    ("FP-ANNO", 5, "Continuous", 0.18, True),
    ("C-TOPO", 4, "Continuous", 0.13, True),
    ("C-ROAD", 2, "Continuous", 0.35, True),
    ("C-PLNT", 3, "Continuous", 0.18, True),
    ("C-ANNO", 5, "Continuous", 0.18, True),
]


REQUIRED_LAYERS = {layer[0] for layer in LAYERS}


def set_header_var(header, key: str, value) -> None:
    try:
        header[key] = value
    except DXFKeyError:
        # Some vars are version-dependent; skip unsupported keys.
        pass


def ensure_linetypes(doc: ezdxf.document.Drawing) -> None:
    if "Dashed" not in doc.linetypes:
        doc.linetypes.add("Dashed", pattern=[0.5, -0.25], description="Dashed __ __ __")
    if "Center" not in doc.linetypes:
        doc.linetypes.add("Center", pattern=[1.25, -0.25, 0.25, -0.25], description="Center ____ _ ____ _")
    if "Hidden" not in doc.linetypes:
        doc.linetypes.add("Hidden", pattern=[0.25, -0.125], description="Hidden __ __ __")


def set_headers(doc: ezdxf.document.Drawing) -> None:
    header = doc.header
    set_header_var(header, "$MEASUREMENT", 0)
    set_header_var(header, "$INSUNITS", 1)
    set_header_var(header, "$LUNITS", 2)
    set_header_var(header, "$LUPREC", 4)
    set_header_var(header, "$TEXTSIZE", 0.125)

    set_header_var(header, "$LTSCALE", 1.0)
    set_header_var(header, "$CELTSCALE", 1.0)
    set_header_var(header, "$PSLTSCALE", 1)
    set_header_var(header, "$MSLTSCALE", 1)

    set_header_var(header, "$TEXTSTYLE", TEXT_STYLE_STD)
    set_header_var(header, "$DIMSTYLE", DIM_STYLE_STD)
    set_header_var(header, "$DIMTXSTY", TEXT_STYLE_STD)
    set_header_var(header, "$DIMASSOC", 2)

    set_header_var(header, "$CANNOSCALE", ANNO_SCALE)
    set_header_var(header, "$ANNOAUTOSCALE", 0)
    set_header_var(header, "$ANNOALLVISIBLE", 0)

    set_header_var(header, "$DIMTXT", 0.125)
    set_header_var(header, "$DIMASZ", 0.125)
    set_header_var(header, "$DIMSCALE", 1.0)
    set_header_var(header, "$DIMGAP", 0.0625)
    set_header_var(header, "$DIMCLRD", 6)
    set_header_var(header, "$DIMCLRE", 6)
    set_header_var(header, "$DIMCLRT", 6)
    set_header_var(header, "$DIMLUNIT", 4)

    set_header_var(header, "$LIMMIN", (0, 0))
    set_header_var(header, "$LIMMAX", (36, 24))
    set_header_var(header, "$EXTMIN", (0, 0, 0))
    set_header_var(header, "$EXTMAX", (36, 24, 0))


def ensure_text_styles(doc: ezdxf.document.Drawing) -> None:
    if TEXT_STYLE_STD not in doc.styles:
        doc.styles.add(TEXT_STYLE_STD, font="txt")
    if TEXT_STYLE_ANNO not in doc.styles:
        doc.styles.add(TEXT_STYLE_ANNO, font="txt")


def ensure_dim_styles(doc: ezdxf.document.Drawing) -> None:
    def setup_common(style) -> None:
        style.dxf.dimtxsty = TEXT_STYLE_STD
        style.dxf.dimtxt = 0.125
        style.dxf.dimasz = 0.125
        style.dxf.dimgap = 0.0625
        style.dxf.dimclrd = 6
        style.dxf.dimclre = 6
        style.dxf.dimclrt = 6
        style.dxf.dimlunit = 4

    std = (
        doc.dimstyles.duplicate_entry("Standard", DIM_STYLE_STD)
        if DIM_STYLE_STD not in doc.dimstyles
        else doc.dimstyles.get(DIM_STYLE_STD)
    )
    setup_common(std)
    std.dxf.dimscale = 1.0
    std.dxf.dimtix = 0
    std.dxf.dimatfit = 3

    anno = (
        doc.dimstyles.duplicate_entry("Standard", DIM_STYLE_ANNO)
        if DIM_STYLE_ANNO not in doc.dimstyles
        else doc.dimstyles.get(DIM_STYLE_ANNO)
    )
    setup_common(anno)
    anno.dxf.dimscale = 0.0
    anno.dxf.dimtix = 0
    anno.dxf.dimatfit = 3


def ensure_layers(doc: ezdxf.document.Drawing) -> None:
    for name, color, linetype, lineweight_mm, plot in LAYERS:
        lw = int(round(lineweight_mm * 100))
        if name in doc.layers:
            layer = doc.layers.get(name)
            layer.color = color
            layer.linetype = linetype
            layer.dxf.lineweight = lw
            layer.dxf.plot = 1 if plot else 0
        else:
            doc.layers.add(name=name, color=color, linetype=linetype, lineweight=lw, plot=plot)


def draw_geometry(doc: ezdxf.document.Drawing) -> None:
    msp = doc.modelspace()

    # Arch D border 36x24
    msp.add_lwpolyline([(0, 0), (36, 0), (36, 24), (0, 24), (0, 0)], dxfattribs={"layer": "A-BORDER"})
    # Inner margin offset 0.5
    msp.add_lwpolyline([(0.5, 0.5), (35.5, 0.5), (35.5, 23.5), (0.5, 23.5), (0.5, 0.5)], dxfattribs={"layer": "A-BORDER"})

    # Title block: lower-right 14x7.5
    x0, y0, x1, y1 = 22.0, 0.0, 36.0, 7.5
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], dxfattribs={"layer": "A-TTLB"})
    msp.add_line((30.0, y0), (30.0, y1), dxfattribs={"layer": "A-TTLB"})
    msp.add_line((x0, 6.0), (x1, 6.0), dxfattribs={"layer": "A-TTLB"})
    msp.add_line((x0, 3.0), (x1, 3.0), dxfattribs={"layer": "A-TTLB"})

    for text, pos in [
        ("PROJECT", (22.4, 6.45)),
        ("DRAWING TITLE", (22.4, 3.45)),
        ("SHEET", (30.4, 6.45)),
        ("DATE", (30.4, 4.2)),
        ("SCALE", (30.4, 1.2)),
    ]:
        msp.add_text(
            text,
            dxfattribs={
                "layer": "A-TTLB",
                "height": 0.18,
                "style": TEXT_STYLE_STD,
            },
        ).set_placement(pos, align=TextEntityAlignment.LEFT)


def build_document() -> ezdxf.document.Drawing:
    # AC1032 is more robust for modern AutoCAD variants.
    doc = ezdxf.new("R2018")
    set_headers(doc)
    ensure_linetypes(doc)
    ensure_text_styles(doc)
    ensure_dim_styles(doc)
    ensure_layers(doc)
    draw_geometry(doc)
    return doc


def verify_output(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        doc = ezdxf.readfile(path)
    except Exception as exc:
        return [f"DXF parse failure: {exc}"]

    header = doc.header
    required = {
        "$MEASUREMENT": 0,
        "$INSUNITS": 1,
        "$LUNITS": 2,
        "$LUPREC": 4,
        "$TEXTSTYLE": TEXT_STYLE_STD,
        "$DIMSTYLE": DIM_STYLE_STD,
        "$DIMTXSTY": TEXT_STYLE_STD,
        "$DIMASSOC": 2,
        "$LTSCALE": 1.0,
        "$CELTSCALE": 1.0,
        "$PSLTSCALE": 1,
    }
    for key, value in required.items():
        if header.get(key) != value:
            errors.append(f"{key}={header.get(key)!r}, expected {value!r}")

    optional = {
        "$MSLTSCALE": 1,
        "$CANNOSCALE": ANNO_SCALE,
        "$ANNOAUTOSCALE": 0,
        "$ANNOALLVISIBLE": 0,
    }
    for key, value in optional.items():
        if key in header and header.get(key) != value:
            errors.append(f"{key}={header.get(key)!r}, expected {value!r}")

    for lt in ("Continuous", "Dashed", "Center", "Hidden"):
        if lt not in doc.linetypes:
            errors.append(f"Missing linetype: {lt}")

    for layer in REQUIRED_LAYERS:
        if layer not in doc.layers:
            errors.append(f"Missing layer: {layer}")

    for style in (TEXT_STYLE_STD, TEXT_STYLE_ANNO):
        if style not in doc.styles:
            errors.append(f"Missing text style: {style}")

    for dstyle in (DIM_STYLE_STD, DIM_STYLE_ANNO):
        if dstyle not in doc.dimstyles:
            errors.append(f"Missing dim style: {dstyle}")

    texts = {entity.plain_text() for entity in doc.modelspace().query("TEXT")}
    for label in ("PROJECT", "DRAWING TITLE", "SHEET", "DATE", "SCALE"):
        if label not in texts:
            errors.append(f"Missing title block label: {label}")

    if len(list(doc.modelspace())) == 0:
        errors.append("Modelspace has no entities")

    return errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Parse and validate generated DXF.")
    args = parser.parse_args(argv)

    out_path = Path(__file__).resolve().parent / OUTPUT_FILENAME
    doc = build_document()
    doc.saveas(out_path)

    if args.verify:
        errors = verify_output(out_path)
        if errors:
            print("Verification failed:", file=sys.stderr)
            for err in errors:
                print(f"- {err}", file=sys.stderr)
            print(str(out_path.resolve()))
            return 1
        print("Verification passed")

    print(str(out_path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
