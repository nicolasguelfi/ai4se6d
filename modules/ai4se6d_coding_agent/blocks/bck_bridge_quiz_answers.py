"""Slide — Hands-up quiz — answers."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Hands-up quiz — answers — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "bridge_quiz_answers_body")
    keyword = s.bold + s.project.colors.highlight
    number = Style.create(s.bold + s.project.colors.highlight + s.center_txt, "bridge_quiz_answers_num")
bs = BlockStyles

_NOTES = [
    ("1 — Yes",
     "RED first is the normal start of test-driven development: a new test must fail before the code exists."),
    ("2 — No",
     "The golden rule: you review the test between RED and GREEN. A test written with its code in one go may "
     "only prove that the code does what it does."),
    ("3 — No",
     "Tests that survive sabotage prove nothing: fix the tests, not the code."),
    ("4 — No",
     "200-400 lines per review: a 1,200-line diff is reviewed per task, in several passes."),
    ("5 — Yes",
     "You may refuse a finding of the AI review, with a written reason: you are the judge, not the agent."),
]

_ANSWERS = [
    ((bs.keyword, 'Yes'), ' — RED first is the normal start'),
    ((bs.keyword, 'No'), ' — golden rule: you review the test between RED and GREEN'),
    ((bs.keyword, 'No'), ' — they prove nothing: fix the tests'),
    ((bs.keyword, 'No'), ' — 200-400 lines per review: review per task'),
    ((bs.keyword, 'Yes'), ' — with a written reason'),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Quiz — Answers', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Quiz — Answers", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One numbered row per answer, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_ANSWERS), cols, filled=(2, 3))
        with st_zoom(124), st_grid(cols=cols, gap="4.5vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(_ANSWERS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
