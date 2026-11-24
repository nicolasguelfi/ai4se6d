"""Slide — Questions on any project (16:30, 20 min): prompts for learners + the trainer's SE questions."""
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
     "Learners do it — aloud, in plenary. 20 minutes of questions on ANY project seen at 15:30. Start with the "
     "learners' own questions; use yours below to open software-engineering topics."),
    ("Your questions — requirements",
     "« Where is the specification? Who wrote it, you or the agent? » · « How do you know the client's feature is "
     "done? » → day 2 (plan.md), day 3 (/gse-reqs)."),
    ("Your questions — architecture",
     "« What is the architecture? Which files, why? » · « Where is the data kept? » · « Could a colleague take over "
     "tomorrow? » → day 2 (AGENTS.md, structure), day 3."),
    ("Your questions — tests",
     "« What is the test coverage? » · « What is your test method — did you test by hand, how? » · « After the "
     "client's feature, how do you know v1 still works? » (regression) → day 2 (TDD), day 4 (quality)."),
    ("Your questions — code and history",
     "« Who read the code? » · « What do your commits tell? » · « What did the agent do that you did not ask "
     "for? » → day 2 (git, AI code review)."),
    ("Your questions — production",
     "« Would you give it to a client tomorrow? Why not? » · « How would it go to production? » · « What does it "
     "cost (tokens)? Which licences? » → days 4-6 (CI, deployment, ethics)."),
    ("Your questions — process",
     "« Through which phases did you go? Which did your slides show, which did they skip? » → the hidden goal of "
     "the presentation; link to the morning cycles at 16:50."),
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
                st_write(bs.heading, "Questions on Any Project", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Questions on Any Project", entries=_NOTES,
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
                    st_write(bs.body, (bs.label, "Any project you saw — for example:"), tag=t.div)
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
