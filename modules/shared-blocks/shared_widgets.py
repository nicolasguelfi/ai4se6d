"""Shared interactive widgets for all training modules.

These widgets use st.html() for CSS-based interactivity (hover, transitions)
that cannot be achieved with pure StreamTeX rendering functions.
"""
import hashlib
import streamlit as st


# ── Default styles ───────────────────────────────────────────────────────
_DEFAULT_SCALE = "1.8vw"
_DEFAULT_TITLE_COLOR = "#7AB8F5"
_DEFAULT_TERM_COLOR = "#7AB8F5"
_DEFAULT_DEF_COLOR = "#ccc"


def _build_font_style(scale: str, ratio: float, color: str, extra: str = "") -> str:
    """Build a CSS font style from scale, ratio, and color."""
    return f"font-size:calc({ratio} * {scale}); color:{color}; {extra}"


def st_hover_tooltip(
    icon: str = "\u2139\uFE0F",
    title: str = "",
    entries: list[tuple[str, str]] | None = None,
    *,
    scale: str = _DEFAULT_SCALE,
    title_style: str | None = None,
    term_style: str | None = None,
    def_style: str | None = None,
    width: str = "40vw",
    height: str = "auto",
    position: str = "center",
    direction: str = "down",
    bg_color: str = "rgba(17,17,17,0.94)",
):
    """Render an inline icon that reveals a tooltip panel on hover.

    Args:
        icon: Emoji or character displayed inline (e.g. "ℹ️", "💡").
        title: Tooltip panel title text.
        entries: List of (term, definition) tuples shown in the panel.
        scale: Base font unit (any CSS unit). Title=1.3x, term=1.1x, def=1.0x.
        title_style: CSS override for the panel title (wins over scale).
        term_style: CSS override for each entry term (wins over scale).
        def_style: CSS override for each entry definition (wins over scale).
        width: CSS width of the tooltip panel (e.g. "40vw", "520px").
        height: CSS height of the tooltip panel (e.g. "auto", "30vh").
        position: Horizontal alignment — "right" | "left" | "center".
        direction: Vertical direction — "down" (opens below icon) | "up" (opens above icon).
        bg_color: CSS background color of the tooltip panel.
    """
    # Compute styles from scale (explicit style wins if provided)
    if title_style is None:
        title_style = _build_font_style(scale, 1.3, _DEFAULT_TITLE_COLOR, "font-weight:700;")
    if term_style is None:
        term_style = _build_font_style(scale, 1.1, _DEFAULT_TERM_COLOR, "font-weight:700;")
    if def_style is None:
        def_style = _build_font_style(scale, 1.0, _DEFAULT_DEF_COLOR, "line-height:1.45;")
    if entries is None:
        entries = []

    # Unique ID to avoid CSS collisions when multiple tooltips on same page
    uid = hashlib.md5(f"{title}_{icon}_{len(entries)}".encode()).hexdigest()[:8]
    cls = f"stx-tt-{uid}"

    # Horizontal position CSS for the panel
    # "left" = panel opens toward the left (anchored right)
    # "right" = panel opens toward the right (anchored left)
    if position == "left":
        pos_h_css = "right: 0;"
    elif position == "center":
        pos_h_css = "left: 50%; transform: translateX(-50%);"
    else:
        pos_h_css = "left: 0;"

    # Vertical direction CSS for the panel
    # "down" = panel opens below icon (default)
    # "up" = panel opens above icon
    if direction == "up":
        pos_v_css = "bottom: 2.2rem;"
    else:
        pos_v_css = "top: 2.2rem;"

    # Build entries HTML
    entries_html = ""
    for term, definition in entries:
        entries_html += (
            f'<div style="margin-bottom:0.5rem;">'
            f'<span style="{term_style}">{term}</span>'
            f'<span style="{def_style}"> &mdash; {definition}</span>'
            f'</div>'
        )

    html = f"""
    <style>
    .{cls} {{
        display: inline-block;
        position: relative;
        vertical-align: middle;
        margin-left: 0.4em;
        cursor: help;
    }}
    .{cls} .{cls}-icon {{
        font-size: 1.6rem;
        opacity: 0.7;
        transition: opacity 0.2s;
    }}
    .{cls}:hover .{cls}-icon {{ opacity: 1; }}
    .{cls} .{cls}-body {{
        display: none;
        position: absolute;
        {pos_v_css}
        {pos_h_css}
        z-index: 100;
        width: {width};
        height: {height};
        overflow-y: auto;
        background: {bg_color};
        border: 1px solid rgba(122,184,245,0.3);
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        text-align: left;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    }}
    .{cls}:hover .{cls}-body {{ display: block; }}
    </style>

    <span class="{cls}">
        <span class="{cls}-icon">{icon}</span>
        <div class="{cls}-body">
            <div style="{title_style} margin-bottom:0.6rem;">{icon} {title}</div>
            {entries_html}
        </div>
    </span>
    """

    st.html(html)
