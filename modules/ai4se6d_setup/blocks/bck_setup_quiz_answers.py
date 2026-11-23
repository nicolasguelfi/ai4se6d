"""Slide — Hands-up quiz answers (statements on the previous slide, bck_setup_quiz)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Quiz answers styles."""
    heading = s.project.titles.slide_title + s.center_txt
    true_label = Style.create(s.project.titles.body + s.bold + s.project.colors.success, "setup_quiz_true_body")
    false_label = Style.create(s.project.titles.body + s.bold + s.project.colors.critical, "setup_quiz_false_body")
    why = s.project.titles.body
bs = BlockStyles

# (answer, one-line reason) — same order as _STATEMENTS in bck_setup_quiz.py.
_ANSWERS = [
    (False, "No memory: the context is resent every time."),
    (True, "Long chats, big files cost more. Key capped."),
    (False, "Never: a prompt leaves your machine."),
    (True, "The definition — and your afternoon."),
    (True, "Tomorrow: a commit after every step."),
]

_NOTES = [
    ("The message",
     "The five answers, in the order of the statements, each with a one-line reason."),
    ("1 — FALSE",
     "The model has no memory: the whole context is resent with every request. That is also why long chats cost more."),
    ("2 — TRUE",
     "Every token sent and received is paid: long chats and big files cost more. The participants' keys are capped."),
    ("3 — FALSE",
     "Never paste a key (or any secret) in a prompt: a prompt leaves your machine."),
    ("4 and 5 — TRUE",
     "Vibe coding = accepting AI code unread — the definition, and what they did this afternoon. A commit is a "
     "save point: tomorrow, one after every step."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Quiz — Answers", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Quiz Answers", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One row per answer, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 19% 71% 5%"
        cells = s.project.containers.rows(len(_ANSWERS), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
            for i, (answer, why) in enumerate(_ANSWERS, start=1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.true_label if answer else bs.false_label, f"{i} · {'TRUE' if answer else 'FALSE'}",
                             tag=t.div)
                with g.cell():
                    st_write(bs.why, why, tag=t.div)
                with g.cell():
                    pass  # right margin
