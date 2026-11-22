"""Shared interactive widgets for all training modules.

st_hover_tooltip now delegates to the StreamTeX library's own ``st_hover_tooltip`` (since 0.7.8),
the one streamtex-all-trainings uses (NG, 2026-11-22): the panel is capped at ``max_height``
(default 80vh) and scrolls with a visible, wide scrollbar instead of running off the slide.
The 112 blocks that import it from here keep their calls unchanged.
"""
from streamtex import st_hover_tooltip as _stx_hover_tooltip


# ── Default styles (same values as the library) ──────────────────────────
_DEFAULT_SCALE = "1.8vw"


def st_hover_tooltip(
    icon: str = "ℹ️",
    title: str = "",
    entries: list[tuple[str, str]] | None = None,
    *,
    scale: str = _DEFAULT_SCALE,
    title_style: str | None = None,
    term_style: str | None = None,
    def_style: str | None = None,
    width: str = "50vw",
    height: str = "auto",
    max_height: str = "80vh",
    position: str = "left",
    direction: str = "down",
    bg_color: str = "rgba(17,17,17,0.94)",
) -> None:
    """Inline "i" icon revealing a panel of (term, definition) entries on hover.

    Thin wrapper over ``streamtex.st_hover_tooltip`` with the reference defaults
    (streamtex-all-trainings: ``position="left"``, ``direction="down"``, ``width="50vw"``).
    ``max_height`` caps the panel; longer notes scroll with a visible scrollbar.
    """
    _stx_hover_tooltip(
        icon, title, entries,
        scale=scale, title_style=title_style, term_style=term_style, def_style=def_style,
        width=width, height=height, max_height=max_height,
        position=position, direction=direction, bg_color=bg_color,
    )
