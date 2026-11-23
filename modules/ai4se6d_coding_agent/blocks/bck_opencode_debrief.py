"""Slide — opencode debrief (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    pair = Style.create(s.project.titles.body_accent + s.center_txt, "ocdeb_pair")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — in pairs, out loud. Ask the two questions, then neighbours compare their /budgets plans: "
     "same files? same tests?"),
    ("The message",
     "Five minutes to turn the three try-its into lessons: what context changed, and what the plan agent taught."),
    ("Question 1",
     "Collect concrete differences in the answers once AGENTS.md and @files were there (test command, folders, "
     "the €25.50 format)."),
    ("Question 2",
     "Collect what the plan agent asked and what participants pushed back on: tests first? smaller steps?"),
    ("Pairs",
     "Neighbours compare their plans: same files? same tests? why not? Differences show what each prompt left "
     "open."),
    ("Link to the next session",
     "The planning workshop at 11:00 writes the real plan of CalcApp v0.1 in docs/plan.md."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Debrief — 5 min", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Debrief — 5 min", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "8vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ("What changed in the answers once ", (bs.keyword, "AGENTS.md"), " and ", (bs.keyword, "@files"),
             " were there?"),
            ("What did the ", (bs.keyword, "plan agent"), " ask you — and what did you push back on?"),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(125), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "10vh")
        with st_zoom(125):
            st_write(bs.pair, "Compare plans with your neighbour: same files? same tests? why not?", tag=t.div)
