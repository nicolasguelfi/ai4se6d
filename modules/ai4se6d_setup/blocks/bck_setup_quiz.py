"""Slide — Hands-up quiz on day 1: five true/false statements (answers on the next slide)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Quiz slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    number = s.bold + s.project.colors.highlight
    keyword = s.bold + s.project.colors.highlight
bs = BlockStyles

# Keep in the same order as _ANSWERS in bck_setup_quiz_answers.py (next slide).
_STATEMENTS = [
    "The model remembers yesterday's chat.",
    "Every token sent and received costs money.",
    "Pasting your API key in a prompt is fine.",
    "Vibe coding = accepting AI code unread.",
    "A commit is a save point you can return to.",
]

_NOTES = [
    ("Trainer action",
     "Learners do it — hands up for TRUE. Read each of the five statements and count the hands; give no "
     "answer before the next slide."),
    ("The message",
     "Five true/false statements on day 1: hands up for TRUE. Answers on the next slide."),
    ("What it checks",
     "Memory and context, cost per token, key safety, what vibe coding means, and git as save points — one "
     "statement per idea of the day."),
    ("How to run it",
     "Read each statement, count the hands, do NOT give the answer yet: the next slide gives all five with "
     "a one-line reason."),
    ("The trap",
     "Statement 4 sounds like a criticism, but it is the definition of vibe coding — and exactly what the "
     "participants did this afternoon."),
    ("Ask the room",
     "« Who changed their mind between this morning and now on one of these? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Hands-Up Quiz", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Hands-Up Quiz", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One numbered row per statement, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_STATEMENTS), cols, filled=(2, 3))
        with st_zoom(115):
            with st_grid(cols="5% 90% 5%", cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.body, "True or false? ", (bs.keyword, "Hands up for TRUE."), tag=t.div)
                with g.cell():
                    pass
            st_space("v", "3vh")
            with st_grid(cols=cols, gap="5vh 0.5vw", cell_styles=cells) as g:
                for n, statement in enumerate(_STATEMENTS, 1):
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body + bs.number, f"{n}", tag=t.div)
                    with g.cell():
                        st_write(bs.body, statement, tag=t.div)
                    with g.cell():
                        pass  # right margin
