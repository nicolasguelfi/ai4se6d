"""Slide — Debrief — review practice."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief — review practice — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_debrief_body")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_ex_debrief_timer")
    number = Style.create(s.bold + s.project.colors.highlight + s.center_txt, "review_ex_debrief_num")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — they answer aloud. Debrief 16:05 → 16:15: two questions to the room, then "
     "neighbours compare their findings."),
    ("The message",
     "Ten minutes to share what the review taught: what the AI found, what it missed, what you refused."),
    ("Question 1",
     "The most useful finding, and the obvious problem the AI missed: AI review gives breadth, you give depth."),
    ("Question 2",
     "What was refused, and why: refusing with a written reason is a decision, not laziness."),
    ("Compare",
     "Neighbours wrote similar code from the same plan. Similar findings? If not, why — prompt, scope of the "
     "diff, or the model itself?"),
    ("Next",
     "16:15: ship v0.1 — merge, tag, and main takes your work."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(62):
                st_write(bs.heading, 'Debrief — Review (10 min)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Debrief — Review", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(90):
            st_write(bs.timer, '16:05 → 16:15', tag=t.div)
        st_space("v", "4vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        questions = [
            'Most useful finding? What obvious problem did the AI miss?',
            'What did you refuse, and why?',
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
        st_space("v", "6vh")
        with st_zoom(115), st_block(s.project.containers.callout):
            st_write(bs.body, 'Compare with your neighbour: similar code, similar findings? Why not?')
