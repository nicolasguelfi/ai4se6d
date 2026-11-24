"""Slide — What we covered yesterday (day 1 recap)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Recap slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    question = Style.create(s.project.titles.body_accent + s.center_txt, "recap_question")
bs = BlockStyles

_NOTES = [
    ("The message",
     "A two-minute recap of day 1 before changing gear: what an LLM can and cannot do, VibeCoding vs "
     "VibeEngineering, the tools, the set-up, and the FreeSelfApp prototype."),
    ("What participants have now",
     "Each one has opencode, their key, GSE-One, a tutor window and GitHub — today reuses all of them."),
    ("The trap",
     "FreeSelfApp was built fast and naively: it runs, but nobody planned it, tested it or reviewed it."),
    ("Link to today",
     "The hands-up question opens day 2: today rebuilds an app (CalcApp) with engineering discipline."),
    ("Ask the room",
     "« Hands up: who would ship it to a customer? » — then « why not? »: the answers are today's agenda."),
]

_ITEMS = [
    ((bs.keyword, "GenAI basics"), " — what an LLM can and cannot do"),
    ((bs.keyword, "VibeCoding"), " vs ", (bs.keyword, "VibeEngineering")),
    ((bs.keyword, "Tools"), " — opencode is our coding agent"),
    ((bs.keyword, "Set-up"), " — your key, GSE-One, your ", (bs.keyword, "tutor window"), ", GitHub"),
    ((bs.keyword, "FreeSelfApp"), " — a naive prototype, built fast"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "What We Covered Yesterday", tag=t.div, toc_lvl="1", label="Welcome")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What We Covered Yesterday", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # one row per topic, alternating fills — motif L2 + fonds f1 (margins 5 %)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(106), st_grid(cols=cols, gap="5vh 0.5vw", cell_styles=cells) as g:
            for item in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *item, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "7vh")
        with st_zoom(134):
            st_write(bs.question, "Hands up: who would ship it to a customer?", tag=t.div)
