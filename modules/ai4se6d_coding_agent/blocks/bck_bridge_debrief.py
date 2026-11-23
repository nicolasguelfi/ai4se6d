"""Slide — Debrief — the whole day."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief — the whole day — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "bridge_debrief_body")
    number = Style.create(s.bold + s.project.colors.highlight + s.center_txt, "bridge_debrief_num")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Ten minutes on the whole day: plan, test first, build, review, ship — which step was skipped, and which "
     "one must stay human."),
    ("Question 1",
     "The step skipped or rushed, and what it cost: a missing test found late, a review of a diff too big, a "
     "plan too vague for the agent."),
    ("Question 2",
     "What to hand to a tool and what must stay yours. It prepares tomorrow: GSE-One automates the loop, but "
     "the decisions stay with you."),
    ("How",
     "Compare with your neighbour first, then 2-3 answers for the room."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(62):
                st_write(bs.heading, 'Debrief — the Day (10 min)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Debrief — the Day", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "6vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        questions = [
            'Which step of the loop did you skip or rush? What did it cost you?',
            'Which step would you hand to a tool — and which must stay yours?',
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(questions), cols, filled=(2, 3))
        with st_zoom(115), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, q in enumerate(questions, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, q, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "8vh")
        with st_zoom(115), st_block(s.project.containers.callout):
            st_write(bs.body, 'Compare with your neighbour, then 2-3 answers for the room.')
