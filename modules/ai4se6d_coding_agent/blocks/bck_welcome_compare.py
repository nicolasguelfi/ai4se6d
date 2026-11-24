"""Slide — Day 1 vs Day 2 comparison table."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Comparison table styles."""
    heading = s.project.titles.heading
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    today = Style.create(s.project.titles.table_cell + s.project.colors.highlight, "compare_today")
bs = BlockStyles

_HEADER = ("", "Day 1 — yesterday", "Day 2 — today")
_ROWS = [
    ("Mindset", "Explore, move fast", "Plan, then build"),
    ("Output", "FreeSelfApp, a prototype", "CalcApp v0.1, tested"),
    ("Approach", "“Let the AI figure it out”", "“Guide the AI with intent”"),
    ("Tests", "None, or very few", "Test first, every task"),
    ("Safety net", "None", "Git: commit, branch"),
    ("Plan", "In your head", "docs/plan.md, committed"),
]

_NOTES = [
    ("The message",
     "The same participants, the same agent, two ways of working. Each row is one habit that changes today."),
    ("Read it row by row",
     "Mindset: explore → plan, then build. Output: a prototype → CalcApp v0.1, tested. Approach: let the AI figure "
     "it out → guide it with intent."),
    ("The safety rows",
     "Tests: none → test first, every task. Safety net: none → Git commit and branch. Plan: in your head → "
     "docs/plan.md, committed in the repository."),
    ("The trap",
     "Reading day 1 as « wrong »: exploring fast is fine for a prototype. Day 2 is what it takes to ship."),
    ("Link to the day",
     "Each right-hand cell is one session of the day: Git first, technical planning, the build with tests, the "
     "review, the delivery."),
    ("Ask the room",
     "« Which row would have saved you the most time yesterday? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Day 1 vs Day 2", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Day 1 vs Day 2", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # header row + one row per habit, alternating fills — motif L2 + fonds f1 (margins 5 %)
        cols = "5% 20% 35% 35% 5%"
        cells = s.project.containers.rows(1 + len(_ROWS), cols, filled=(2, 3, 4))
        with st_zoom(110), st_grid(cols=cols, gap="3.4vh 0.4vw", cell_styles=cells) as g:
            for i, row in enumerate([_HEADER] + _ROWS):
                with g.cell():
                    pass  # left margin
                for j, text in enumerate(row):
                    with g.cell():
                        style = bs.th if i == 0 else (bs.tl if j == 0 else (bs.today if j == 2 else bs.td))
                        st_write(style, text, tag=t.div)
                with g.cell():
                    pass  # right margin
