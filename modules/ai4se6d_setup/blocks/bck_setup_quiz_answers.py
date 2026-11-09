"""Slide — Hands-up quiz answers (statements on the previous slide, bck_setup_quiz)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Quiz answers styles."""
    heading = s.project.titles.slide_title + s.center_txt
    true_label = Style.create(s.project.titles.table_label + s.project.colors.success, "setup_quiz_true")
    false_label = Style.create(s.project.titles.table_label + s.project.colors.critical, "setup_quiz_false")
    why = s.project.titles.table_cell
bs = BlockStyles

# (answer, one-line reason) — same order as _STATEMENTS in bck_setup_quiz.py.
_ANSWERS = [
    (False, "No memory: the context is resent every time."),
    (True, "Long chats, big files cost more. Key capped."),
    (False, "Never: a prompt leaves your machine."),
    (True, "The definition — and your afternoon."),
    (True, "Tomorrow: a commit after every step."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Quiz — Answers", tag=t.div, toc_lvl="1")
        with st_grid(cols="auto 1fr", gap="12px 24px", cell_styles=s.project.containers.cell_pad_sm) as g:
            for i, (answer, why) in enumerate(_ANSWERS, start=1):
                with g.cell():
                    st_write(bs.true_label if answer else bs.false_label, f"{i} · {'TRUE' if answer else 'FALSE'}")
                with g.cell():
                    st_write(bs.why, why)
