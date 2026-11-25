"""Slide — Planning debrief: share and review (5 min)."""
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
    number = s.bold + s.project.colors.highlight
    pair = Style.create(s.project.titles.body_accent + s.center_txt, "plandeb_pair")
    next_step = Style.create(s.project.titles.body + s.project.colors.highlight + s.bold + s.center_txt, "plandeb_next")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — in pairs, out loud. Ask the two questions, then neighbours compare plans: different is "
     "fine, both must be testable."),
    ("The message",
     "Five minutes to compare plans before building: what the agent brought, what you changed."),
    ("Question 1",
     "What did the plan agent ask or propose that you had not thought of? This is the value of eliciting first."),
    ("Question 2",
     "Which user story did you split into development tasks, or which development task did you rewrite — and why? This is the human part of the plan."),
    ("With the neighbour",
     "Different plans are normal: the test is not « same tasks » but « are both testable? »."),
    ("Link to what follows",
     "11:30 — TDD on the [next] task, on its own branch."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Debrief — 5 min", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Debrief — 5 min", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        questions = [
            "What did the plan agent ask or propose that you had not thought of?",
            "Which user story did you split, or which development task did you rewrite — and why?",
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(questions), cols, filled=(2, 3))
        with st_zoom(120), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for n, q in enumerate(questions, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, q, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "2.5vh")
        with st_zoom(122):
            st_write(bs.pair, "Compare with your neighbour: different plans are normal. Are both testable?", tag=t.div)
            st_space("v", "3vh")
            st_write(bs.next_step, "11:30 — TDD on your [next] task, on its own branch.", tag=t.div)
