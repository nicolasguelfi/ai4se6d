"""Slide — Debrief — Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief — Part 2 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_debrief_body")
    timer = Style.create(s.project.titles.stat + s.center_txt, "tasks_debrief_timer")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Learners do it — they answer aloud. Debrief 14:20 → 14:30: two questions to the room, then "
     "neighbours compare their code for the same task."),
    ("The message",
     "Ten minutes, 14:20 → 14:30, on what the agent did beyond the request and what the review checklists "
     "really caught."),
    ("Question 1",
     "Collect the cases where the agent changed a test or did more than asked — the evidence that the GREEN "
     "prompt's « Do not modify the test » and the git diff -- tests/ check matter."),
    ("Question 2",
     "Which checklist item caught something real: React state instead of localStorage, <a href> instead of Link, "
     "a test modified…"),
    ("Compare with a neighbour",
     "Same task, same plan, different code: the agent is not deterministic, so the review cannot be skipped."),
    ("Link",
     "The answers lead straight into the AI-assisted code review section."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Debrief — Part 2 (10 min)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Debrief, Part 2", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(100):
            st_write(bs.timer, '14:20 → 14:30', tag=t.div)
        st_space("v", "3vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            'Where did the agent change a test, or do more than you asked?',
            'Which review-checklist item caught something real?',
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(110), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, text in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, text, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(110), st_block(s.project.containers.callout):
            st_write(bs.body, 'Compare with your neighbour: same task, same code? Why not?')
