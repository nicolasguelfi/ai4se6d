"""Slide — Take notes as you build (feeds the 16:15 debrief)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Take notes slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    caption = s.project.titles.caption
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Everyone creates notes.md in their project folder now and writes "
     "the four items while building; it feeds the 16:15 debrief."),
    ("The message",
     "While building, participants keep a notes.md in their project folder: four things to write down."),
    ("Why notes",
     "Without notes, the debrief turns into impressions. With them, each participant brings a concrete example: "
     "a surprise, a breakage, a count of prompts."),
    ("The key question",
     "« What broke — and who fixed it: you or the AI? » It shows how much of the app the participant "
     "actually controls."),
    ("Link to the debrief",
     "At 16:15 the notes feed « By Hand vs. AI » and the three debrief questions."),
    ("Ask the room",
     "« How many prompts do you think you will need? Write your guess now, compare at 16:15. »"),
]

_ITEMS = [
    ("What ", (bs.keyword, "surprised"), " you"),
    ("What ", (bs.keyword, "broke"), " — and who fixed it: you or the AI?"),
    ((bs.keyword, "How many prompts"), " so far"),
    ("One thing you ", (bs.keyword, "would have done by hand")),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Take Notes", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Take Notes", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One row per note to take, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(100):
            with st_grid(cols=cols, cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.body, (bs.label, "In "), (bs.cmd, "notes.md"), (bs.label, " in your folder:"),
                             tag=t.div)
                with g.cell():
                    pass
            st_space("v", "3vh")
            with st_grid(cols=cols, gap="5vh 0.5vw", cell_styles=cells) as g:
                for parts in _ITEMS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "4vh")
            with st_grid(cols=cols, cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.caption, "We use these notes in the debrief at 16:15.", tag=t.div)
                with g.cell():
                    pass
