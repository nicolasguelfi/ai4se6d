"""Slide — Debrief: three questions, neighbour first."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief questions styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    number = s.bold + s.project.colors.highlight
    keyword = s.bold + s.project.colors.accent
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — in pairs, then aloud. 3 minutes with the neighbour on the three questions, then "
     "together in plenary."),
    ("The message",
     "Three questions: 3 minutes with the neighbour first, then together. Pairs first, so everyone has spoken "
     "before the plenary."),
    ("1 — surprise",
     "Good or bad: what the agent did that the participant did not expect (often: it did more than asked)."),
    ("2 — what broke, who fixed it",
     "If the AI fixed everything, did the participant understand the fix? If they fixed it, how?"),
    ("3 — the client question",
     "« Would you give this app to a client tomorrow? Why not? » The answers (no tests, unread code, unknown "
     "decisions, data) are exactly the gap between vibe coding and engineering."),
    ("Link to the next slide",
     "« Back to This Morning » maps these experiences to the morning cycles (CCSET01-03)."),
]

_QUESTIONS = [
    ("When did the agent ", (bs.keyword, "surprise"), " you — good or bad?"),
    ("What ", (bs.keyword, "broke"), ", and who fixed it?"),
    ("Would you give this app to a ", (bs.keyword, "client"), " tomorrow? Why not?"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Three Questions", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Three Questions", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_QUESTIONS), cols, filled=(2, 3))
        with st_zoom(110):
            with st_grid(cols="5% 90% 5%", cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.body, (bs.label, "3 min with your neighbour, then together:"), tag=t.div)
                with g.cell():
                    pass
            st_space("v", "5vh")
            with st_grid(cols=cols, gap="8vh 0.5vw", cell_styles=cells) as g:
                for n, parts in enumerate(_QUESTIONS, 1):
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body + bs.number, f"{n}", tag=t.div)
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
