"""Helper: render a Mermaid diagram with SVG + PDF download buttons underneath.

Exported files (SVG/PNG/PDF) are cached on disk in static/cache/ so they survive
server restarts. Delete a file from the cache to force regeneration.
All cached images have opaque backgrounds (no transparency).
"""
import base64
import hashlib
import io
import re
import urllib.request
import zlib
from pathlib import Path

import streamlit as st
from PIL import Image
import streamtex as stx

_DIAGRAMS_DIR = Path(__file__).resolve().parent.parent / "diagrams"
_CACHE_DIR = Path(__file__).resolve().parent.parent / "static" / "cache"
_KROKI = "https://kroki.io"

_THEME_DARK = "%%{init: {'theme':'dark'}}%%\n"
_THEME_LIGHT = "%%{init: {'theme':'default'}}%%\n"

# Background colors per theme
_BG = {"dark": "#1a1a2e", "light": "#ffffff"}


def _kroki_encode(code: str) -> str:
    compressed = zlib.compress(code.encode("utf-8"), 9)
    return base64.urlsafe_b64encode(compressed).decode("ascii")


def _code_hash(code: str) -> str:
    """Short hash of the diagram code for deterministic filenames."""
    return hashlib.sha256(code.encode("utf-8")).hexdigest()[:12]


def _kroki_fetch(diagram_type: str, fmt: str, code: str) -> bytes:
    """Fetch raw bytes from kroki.io (no caching)."""
    encoded = _kroki_encode(code)
    url = f"{_KROKI}/{diagram_type}/{fmt}/{encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": "StreamTeX/0.2"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


# ── Post-processing: inject opaque backgrounds ──────────────────────


def _svg_with_background(svg_bytes: bytes, bg_color: str) -> bytes:
    """Inject a background color into an SVG element."""
    text = svg_bytes.decode("utf-8")
    # Add style attribute to the <svg> root element
    text = re.sub(
        r"(<svg\b[^>]*)(>)",
        rf'\1 style="background-color: {bg_color}"\2',
        text,
        count=1,
    )
    return text.encode("utf-8")


def _png_with_background(png_bytes: bytes, bg_color: str) -> bytes:
    """Flatten a PNG onto an opaque background."""
    img = Image.open(io.BytesIO(png_bytes))
    if img.mode == "RGBA":
        # Parse hex color
        r = int(bg_color[1:3], 16)
        g = int(bg_color[3:5], 16)
        b = int(bg_color[5:7], 16)
        bg = Image.new("RGBA", img.size, (r, g, b, 255))
        bg.paste(img, mask=img)
        img = bg.convert("RGB")
    elif img.mode != "RGB":
        img = img.convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def _png_bytes_to_pdf(png_bytes: bytes) -> bytes:
    """Convert PNG bytes (already flattened) to PDF."""
    img = Image.open(io.BytesIO(png_bytes))
    if img.mode != "RGB":
        img = img.convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="PDF", resolution=1200.0)
    return buf.getvalue()


# ── Cached fetch with post-processing ───────────────────────────────


def _get_cached(base_hash: str, theme: str, fmt: str) -> bytes | None:
    """Return cached file bytes or None."""
    path = _CACHE_DIR / f"{base_hash}_{theme}.{fmt}"
    if path.exists():
        return path.read_bytes()
    return None


def _put_cache(base_hash: str, theme: str, fmt: str, data: bytes) -> None:
    """Write data to cache."""
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (_CACHE_DIR / f"{base_hash}_{theme}.{fmt}").write_bytes(data)


def _get_svg(raw_code: str, theme: str) -> bytes:
    """Get SVG with opaque background (cached)."""
    directive = _THEME_DARK if theme == "dark" else _THEME_LIGHT
    export_code = directive + raw_code
    h = _code_hash(export_code)

    cached = _get_cached(h, theme, "svg")
    if cached:
        return cached

    raw_svg = _kroki_fetch("mermaid", "svg", export_code)
    svg = _svg_with_background(raw_svg, _BG[theme])
    _put_cache(h, theme, "svg", svg)
    return svg


def _get_png(raw_code: str, theme: str) -> bytes:
    """Get PNG with opaque background (cached)."""
    directive = _THEME_DARK if theme == "dark" else _THEME_LIGHT
    export_code = directive + raw_code
    h = _code_hash(export_code)

    cached = _get_cached(h, theme, "png")
    if cached:
        return cached

    raw_png = _kroki_fetch("mermaid", "png", export_code)
    png = _png_with_background(raw_png, _BG[theme])
    _put_cache(h, theme, "png", png)
    return png


def _get_pdf(raw_code: str, theme: str) -> bytes:
    """Get PDF from flattened PNG (cached)."""
    directive = _THEME_DARK if theme == "dark" else _THEME_LIGHT
    export_code = directive + raw_code
    h = _code_hash(export_code)

    cached = _get_cached(h, theme, "pdf")
    if cached:
        return cached

    png = _get_png(raw_code, theme)
    pdf = _png_bytes_to_pdf(png)
    _put_cache(h, theme, "pdf", pdf)
    return pdf


# ── Public API ──────────────────────────────────────────────────────


def show_diagram(filename: str, *, height: int = 600, key: str = ""):
    """Display a Mermaid diagram + dark/light SVG/PDF download buttons."""
    raw_code = (_DIAGRAMS_DIR / filename).read_text(encoding="utf-8")

    # Browser: light background for readability
    stx.st_mermaid(raw_code, height=height, fit="contain", light_bg=True)

    # Download buttons: dark + light variants (all with opaque backgrounds)
    col1, col2, col3, col4, _pad = st.columns([1, 1, 1, 1, 2])
    with col1:
        try:
            st.download_button(
                "SVG dark", data=_get_svg(raw_code, "dark"),
                file_name=f"{key}_dark.svg", mime="image/svg+xml",
                key=f"svg_dark_{key}",
            )
        except Exception:
            st.caption("SVG dark unavailable")
    with col2:
        try:
            st.download_button(
                "SVG light", data=_get_svg(raw_code, "light"),
                file_name=f"{key}_light.svg", mime="image/svg+xml",
                key=f"svg_light_{key}",
            )
        except Exception:
            st.caption("SVG light unavailable")
    with col3:
        try:
            st.download_button(
                "PDF dark", data=_get_pdf(raw_code, "dark"),
                file_name=f"{key}_dark.pdf", mime="application/pdf",
                key=f"pdf_dark_{key}",
            )
        except Exception:
            st.caption("PDF dark unavailable")
    with col4:
        try:
            st.download_button(
                "PDF light", data=_get_pdf(raw_code, "light"),
                file_name=f"{key}_light.pdf", mime="application/pdf",
                key=f"pdf_light_{key}",
            )
        except Exception:
            st.caption("PDF light unavailable")
