"""Slide — Hands-up quiz — 5 questions."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Hands-up quiz — 5 questions — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "bridge_quiz_body")
    number = Style.create(s.bold + s.project.colors.highlight + s.center_txt, "bridge_quiz_num")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — hands up. Read each question aloud, they raise a hand for « yes »; count, do not "
     "comment yet."),
    ("How to run it",
     "Read each question aloud; hands up for « yes », hands down for « no ». Count, do not comment yet: the "
     "answers are on the next slide."),
    ("What it checks",
     "The day's key rules: RED first, the golden rule (review the test between RED and GREEN), tests that "
     "catch sabotage, review size, and your right to refuse a finding."),
    ("Watch for",
     "Questions where the room splits: come back to them on the answers slide and ask one person from each side "
     "to explain."),
]

_QUESTIONS = [
    'A brand-new test fails before any code exists. Expected?',
    'The agent wrote test + code in one go, all green. Merge without reading?',
    'You sabotage the code and every test still passes. Are the tests useful?',
    'A 1,200-line diff: is one review pass enough?',
    'May you refuse a finding of the AI review?',
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(62):
                st_write(bs.heading, 'Hands-Up Quiz: Yes or No?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Hands-Up Quiz", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_QUESTIONS), cols, filled=(2, 3))
        with st_zoom(105), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, q in enumerate(_QUESTIONS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, q, tag=t.div)
                with g.cell():
                    pass  # right margin
