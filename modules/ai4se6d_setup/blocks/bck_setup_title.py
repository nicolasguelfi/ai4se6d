"""Title slide — Hands-on Setup & First Prototype (day 1 afternoon)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Title slide styles."""
    title = Style.create(
        s.Huge + s.bold + s.center_txt + s.project.colors.primary
        + Style("line-height:1.1;", "setup_title_lh"),
        "setup_title",
    )
    subtitle = Style.create(s.project.titles.subtitle + s.center_txt, "setup_title_subtitle")
    parts = Style.create(s.project.titles.body + s.center_txt, "setup_title_parts")
    part = s.bold + s.project.colors.accent
    info = Style.create(s.project.titles.caption + s.center_txt, "setup_title_info")
bs = BlockStyles

_NOTES = [
    ("The message",
     "This afternoon in three moves: Install your toolchain, Build a first prototype and present it, Debrief together."),
    ("Install",
     "75 min in the room, one step per slide (0 to 8): terminal, opencode 2, Node.js, model key, course kit, "
     "GSE-One v0.93.4, GitHub, check, tutor window."),
    ("Build",
     "The FreeSelfApp workshop: 45 min, 3 iterations (v1, a client's feature, a presentation made by opencode) — no "
     "rules, no plan, on purpose."),
    ("Debrief",
     "9 presentations of 6 min on Google Meet, questions on any project, back to this morning, a hands-up quiz and a "
     "preview of tomorrow."),
    ("Ask the room",
     "« Who has already installed opencode or GSE-One? » — they can help their neighbours during the install."),
]


def build():
    with st_block(s.project.containers.page_fill_center_noalign):
        # title and « i » on the same line, title on ONE line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.title, "Hands-on Setup & First Prototype", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Hands-on Setup & First Prototype", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(150), st_block(s.center_txt):
            st_space("v", "10vh")
            st_write(bs.subtitle, "Day 1 — Afternoon", tag=t.div)
            st_space("v", "9vh")
            st_write(
                bs.parts,
                (bs.part, "Install"), "  →  ", (bs.part, "Build"), "  →  ", (bs.part, "Debrief"),
                tag=t.div,
            )
            st_space("v", "9vh")
            st_write(bs.info, "AI for Software Engineering · opencode 2 + GSE-One v0.93.4", tag=t.div)
