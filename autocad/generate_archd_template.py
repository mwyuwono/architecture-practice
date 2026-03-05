#!/usr/bin/env python3
"""Generate a stable AC1032 AutoCAD template from a validated seed DXF."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf.lldxf.const import DXFKeyError

OUTPUT_FILENAME = "Architectural_Starter_ArchD_AIA_NCS.dxf"
SEED_FILENAME = "seed-archd-annotative.dxf"
TEMPLATES_DIRNAME = "Templates"

TEXT_STYLE_STD = "A-TEXT-STD"
TEXT_STYLE_ANNO = "A-TEXT-ANNO"
DIM_STYLE_STD = "A-DIM-STD"
DIM_STYLE_ANNO = "A-DIM-ANNO"
SEED_DIMSTYLE_SOURCE = "Standard"

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
    ("A-OVERHD", 4, "Hidden", 0.13, True),
    ("A-CNTR", 4, "Center", 0.13, True),
    ("A-ANNO-TEXT", 5, "Continuous", 0.18, True),
    ("A-ANNO-DIMS", 6, "Continuous", 0.18, True),
    ("A-ANNO-TAGS", 5, "Continuous", 0.18, True),
    ("A-ANNO-KEYN", 5, "Continuous", 0.18, True),
    ("A-ANNO-NOTE", 5, "Continuous", 0.18, True),
    ("A-ANNO-GRID", 4, "Center", 0.13, True),
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
REQUIRED_LABELS = {"PROJECT", "DRAWING TITLE", "SHEET", "DATE", "SCALE"}


def set_header_var(header, key: str, value, warnings: list[str]) -> None:
    try:
        header[key] = value
    except DXFKeyError:
        warnings.append(f"Header var unsupported by API/version: {key}")


def linetype_name(name: str) -> str:
    # Keep casing stable for user-facing spec while tolerating seed uppercase defaults.
    return name


def ensure_linetypes(doc: ezdxf.document.Drawing) -> None:
    if "Dashed" not in doc.linetypes and "DASHED" not in doc.linetypes:
        doc.linetypes.add("Dashed", pattern=[0.5, -0.25], description="Dashed __ __ __")
    if "Center" not in doc.linetypes and "CENTER" not in doc.linetypes:
        doc.linetypes.add("Center", pattern=[1.25, -0.25, 0.25, -0.25], description="Center ____ _ ____ _")
    if "Hidden" not in doc.linetypes and "HIDDEN" not in doc.linetypes:
        doc.linetypes.add("Hidden", pattern=[0.25, -0.125], description="Hidden __ __ __")


def set_headers(doc: ezdxf.document.Drawing, warnings: list[str]) -> None:
    header = doc.header
    set_header_var(header, "$MEASUREMENT", 0, warnings)
    set_header_var(header, "$INSUNITS", 1, warnings)
    set_header_var(header, "$LUNITS", 2, warnings)
    set_header_var(header, "$LUPREC", 4, warnings)
    set_header_var(header, "$TEXTSIZE", 0.125, warnings)

    set_header_var(header, "$LTSCALE", 1.0, warnings)
    set_header_var(header, "$CELTSCALE", 1.0, warnings)
    set_header_var(header, "$PSLTSCALE", 1, warnings)

    set_header_var(header, "$TEXTSTYLE", TEXT_STYLE_STD, warnings)
    set_header_var(header, "$DIMSTYLE", DIM_STYLE_STD, warnings)
    set_header_var(header, "$DIMTXSTY", TEXT_STYLE_STD, warnings)
    set_header_var(header, "$DIMASSOC", 2, warnings)

    # Optional/version-dependent: attempt, then report in verify if absent.
    set_header_var(header, "$CANNOSCALE", '1/4"=1\'-0"', warnings)
    set_header_var(header, "$ANNOAUTOSCALE", 0, warnings)
    set_header_var(header, "$ANNOALLVISIBLE", 0, warnings)
    set_header_var(header, "$MSLTSCALE", 1, warnings)

    set_header_var(header, "$DIMTXT", 0.125, warnings)
    set_header_var(header, "$DIMASZ", 0.125, warnings)
    set_header_var(header, "$DIMSCALE", 1.0, warnings)
    set_header_var(header, "$DIMGAP", 0.0625, warnings)
    set_header_var(header, "$DIMCLRD", 6, warnings)
    set_header_var(header, "$DIMCLRE", 6, warnings)
    set_header_var(header, "$DIMCLRT", 6, warnings)
    set_header_var(header, "$DIMLUNIT", 4, warnings)


def ensure_text_styles(doc: ezdxf.document.Drawing) -> None:
    if TEXT_STYLE_STD not in doc.styles:
        doc.styles.add(TEXT_STYLE_STD, font="txt")
    if TEXT_STYLE_ANNO not in doc.styles:
        doc.styles.add(TEXT_STYLE_ANNO, font="txt")


def get_dimstyle_signature(style) -> Dict[str, List[Tuple[int, object]]]:
    signature: Dict[str, List[Tuple[int, object]]] = {}
    data = getattr(style.xdata, "data", {}) if hasattr(style, "xdata") else {}
    for appid, tags in data.items():
        signature[appid] = [(tag.code, tag.value) for tag in tags]
    return signature


def apply_dimstyle_signature(style, signature: Dict[str, List[Tuple[int, object]]]) -> None:
    for appid, tags in signature.items():
        style.set_xdata(appid, tags)


def configure_dimstyle(style, text_style: str, dimscale: float) -> None:
    style.dxf.dimtxsty = text_style
    style.dxf.dimtxt = 0.125
    style.dxf.dimasz = 0.125
    style.dxf.dimgap = 0.0625
    style.dxf.dimclrd = 6
    style.dxf.dimclre = 6
    style.dxf.dimclrt = 6
    style.dxf.dimlunit = 4
    style.dxf.dimscale = dimscale
    style.dxf.dimatfit = 3
    style.dxf.dimtix = 0


def ensure_dim_styles(doc: ezdxf.document.Drawing, seed_doc: ezdxf.document.Drawing) -> Dict[str, List[Tuple[int, object]]]:
    source_name = SEED_DIMSTYLE_SOURCE if SEED_DIMSTYLE_SOURCE in seed_doc.dimstyles else seed_doc.dimstyles.entries[0].dxf.name
    seed_source = seed_doc.dimstyles.get(source_name)
    signature = get_dimstyle_signature(seed_source)

    std = doc.dimstyles.duplicate_entry(source_name, DIM_STYLE_STD)
    configure_dimstyle(std, TEXT_STYLE_STD, 1.0)

    anno = doc.dimstyles.duplicate_entry(source_name, DIM_STYLE_ANNO)
    configure_dimstyle(anno, TEXT_STYLE_ANNO, 0.0)
    if signature:
        apply_dimstyle_signature(anno, signature)

    return signature


def ensure_layers(doc: ezdxf.document.Drawing) -> None:
    for name, color, ltype, lw_mm, plot in LAYERS:
        lw = int(round(lw_mm * 100))
        target_ltype = linetype_name(ltype)
        if name in doc.layers:
            layer = doc.layers.get(name)
            layer.color = color
            layer.linetype = target_ltype
            layer.dxf.lineweight = lw
            layer.dxf.plot = 1 if plot else 0
        else:
            doc.layers.add(name=name, color=color, linetype=target_ltype, lineweight=lw, plot=plot)


def clear_template_layers(doc: ezdxf.document.Drawing) -> None:
    msp = doc.modelspace()
    for entity in list(msp):
        if entity.dxf.hasattr("layer") and entity.dxf.layer in {"A-BORDER", "A-TTLB"}:
            msp.delete_entity(entity)


def draw_geometry(doc: ezdxf.document.Drawing) -> None:
    msp = doc.modelspace()

    msp.add_lwpolyline([(0, 0), (36, 0), (36, 24), (0, 24), (0, 0)], dxfattribs={"layer": "A-BORDER"})
    msp.add_lwpolyline([(0.5, 0.5), (35.5, 0.5), (35.5, 23.5), (0.5, 23.5), (0.5, 0.5)], dxfattribs={"layer": "A-BORDER"})

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
            dxfattribs={"layer": "A-TTLB", "height": 0.18, "style": TEXT_STYLE_STD},
        ).set_placement(pos, align=TextEntityAlignment.LEFT)


def build_document(seed_path: Path) -> tuple[ezdxf.document.Drawing, Dict[str, List[Tuple[int, object]]], list[str]]:
    doc = ezdxf.readfile(seed_path)
    seed_doc = ezdxf.readfile(seed_path)

    warnings: list[str] = []
    set_headers(doc, warnings)
    ensure_linetypes(doc)
    ensure_text_styles(doc)
    seed_signature = ensure_dim_styles(doc, seed_doc)
    ensure_layers(doc)
    clear_template_layers(doc)
    draw_geometry(doc)

    return doc, seed_signature, warnings


def verify_output(path: Path, seed_path: Path, strict_annotative: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        doc = ezdxf.readfile(path)
    except Exception as exc:
        return [f"DXF parse failure: {exc}"], warnings

    if doc.dxfversion != "AC1032":
        errors.append(f"DXF version is {doc.dxfversion}, expected AC1032")

    header = doc.header
    required_header = {
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
    for key, value in required_header.items():
        if header.get(key) != value:
            errors.append(f"{key}={header.get(key)!r}, expected {value!r}")

    for key in ("$CANNOSCALE", "$ANNOAUTOSCALE", "$ANNOALLVISIBLE", "$MSLTSCALE"):
        if key not in header:
            warnings.append(f"Optional annotative header var not present: {key} (seed/object-level handling may apply)")

    for ltype in ("Continuous", "Dashed", "Center", "Hidden"):
        if ltype not in doc.linetypes and ltype.upper() not in doc.linetypes:
            errors.append(f"Missing linetype: {ltype}")

    for layer in REQUIRED_LAYERS:
        if layer not in doc.layers:
            errors.append(f"Missing layer: {layer}")

    for style in (TEXT_STYLE_STD, TEXT_STYLE_ANNO):
        if style not in doc.styles:
            errors.append(f"Missing text style: {style}")

    for dstyle in (DIM_STYLE_STD, DIM_STYLE_ANNO):
        if dstyle not in doc.dimstyles:
            errors.append(f"Missing dim style: {dstyle}")

    if DIM_STYLE_ANNO in doc.dimstyles:
        anno = doc.dimstyles.get(DIM_STYLE_ANNO)
        if anno.dxf.dimtxt != 0.125:
            errors.append(f"{DIM_STYLE_ANNO}.dimtxt={anno.dxf.dimtxt}, expected 0.125")
        if anno.dxf.dimasz != 0.125:
            errors.append(f"{DIM_STYLE_ANNO}.dimasz={anno.dxf.dimasz}, expected 0.125")

    # Compare seed signature against generated A-DIM-ANNO.
    seed_doc = ezdxf.readfile(seed_path)
    seed_src_name = SEED_DIMSTYLE_SOURCE if SEED_DIMSTYLE_SOURCE in seed_doc.dimstyles else seed_doc.dimstyles.entries[0].dxf.name
    seed_signature = get_dimstyle_signature(seed_doc.dimstyles.get(seed_src_name))
    out_signature = get_dimstyle_signature(doc.dimstyles.get(DIM_STYLE_ANNO)) if DIM_STYLE_ANNO in doc.dimstyles else {}

    if seed_signature:
        if not out_signature:
            errors.append("A-DIM-ANNO has no dimstyle xdata signature from seed")
        elif out_signature != seed_signature:
            errors.append("A-DIM-ANNO xdata signature does not match seed dimstyle signature")
    else:
        msg = "Seed dimstyle has no xdata signature to compare; strict annotative verification unavailable"
        if strict_annotative:
            errors.append(msg)
        else:
            warnings.append(msg)

    texts = {entity.plain_text() for entity in doc.modelspace().query("TEXT")}
    for label in REQUIRED_LABELS:
        if label not in texts:
            errors.append(f"Missing title block label: {label}")

    if len(list(doc.modelspace())) == 0:
        errors.append("Modelspace has no entities")

    raw_text = path.read_text(encoding="utf-8", errors="ignore")
    for marker in ("CANNOSCALE", "MSLTSCALE"):
        if marker not in raw_text:
            warnings.append(f"DXF object dictionary marker not found: {marker}")

    return errors, warnings


def main(argv: list[str]) -> int:
    base_dir = Path(__file__).resolve().parent
    templates_dir = base_dir / TEMPLATES_DIRNAME
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Parse and validate generated DXF.")
    parser.add_argument("--strict-annotative", action="store_true", help="Fail if seed annotative signature cannot be verified.")
    parser.add_argument("--seed", type=Path, default=templates_dir / SEED_FILENAME, help="Seed DXF path.")
    args = parser.parse_args(argv)

    seed_path = args.seed.resolve()
    if not seed_path.exists():
        print(f"Seed DXF not found: {seed_path}", file=sys.stderr)
        return 1

    templates_dir.mkdir(parents=True, exist_ok=True)
    out_path = templates_dir / OUTPUT_FILENAME
    doc, _, build_warnings = build_document(seed_path)
    doc.saveas(out_path)

    if args.verify:
        errors, verify_warnings = verify_output(out_path, seed_path, args.strict_annotative)
        warnings = build_warnings + verify_warnings
        if warnings:
            print("Verification warnings:")
            for warning in warnings:
                print(f"- {warning}")
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
