"""Slide — Five habits for an AI-friendly project."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Habits styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("The message",
     "Five cheap habits make a project readable by an agent — and by a new colleague."),
    ("Why each one helps",
     "Descriptive folders and tests mirroring src/ show the agent where code and tests go; the README gives "
     "purpose, stack and commands; a short docs/architecture.md gives the big picture; small files keep each "
     "read focused on one concern."),
    ("The trap",
     "Writing a long architecture document nobody updates. Short and current beats complete and stale."),
    ("Link to the starter",
     "The CalcApp starter already follows these habits: src/pages/, tests/ mirroring src/, docs/ for your plan."),
    ("Ask the room",
     "« Which of the five does your current project miss? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "AI-Friendly Project Habits", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — AI-Friendly Project Habits", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # One numbered row per habit, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.keyword, "Descriptive folders"), " — components/, pages/, utils/"),
            ((bs.keyword, "Tests mirror src/"), " — same path, .test suffix"),
            ((bs.keyword, "A README"), " — purpose, stack, commands"),
            ((bs.keyword, "A short docs/architecture.md"),),
            ((bs.keyword, "Small files"), " — one concern each"),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(134), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
