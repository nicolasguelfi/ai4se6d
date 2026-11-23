"""Slide — Live demo (5 min): what to watch while the trainer drives opencode."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Live demo slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    caption = s.project.titles.caption
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Live demo — you type it in your terminal. 5 min of opencode in an empty folder: one plain sentence, "
     "files created, the agent's questions read aloud, something that runs."),
    ("The message",
     "Five minutes of live demo before the participants start: the trainer drives opencode in an empty folder "
     "and the room watches five things."),
    ("What to show",
     "One plain sentence typed; the agent reading the (empty) folder; files created on their own; the questions "
     "the agent asks and what you answer; something that opens and runs."),
    ("The point to stress",
     "The agent ASKS before some actions: read the request aloud before accepting it — this is the habit the "
     "participants should copy."),
    ("Link to the rest of the afternoon",
     "Right after: the challenge (a small personal web app, by prompting only), three ideas and the first prompts."),
    ("Ask the room",
     "« What did the agent decide without asking me? »"),
]

_WATCH = [
    ("What I type — ", "one plain sentence", ""),
    ("The agent ", "reads the folder", " (empty)"),
    ("It ", "creates files", " on its own"),
    ("What it ", "asks me", " — and what I answer"),
    ("Something I can ", "open and run", ""),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Live Demo — 5 min", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Live Demo", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One row per thing to watch, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_WATCH), cols, filled=(2,))
        with st_zoom(110):
            with st_grid(cols=cols, cell_styles=s.project.containers.row_cell_left) as g:
                with g.cell():
                    pass
                with g.cell():
                    st_write(bs.label, "Watch:", tag=t.div)
                with g.cell():
                    pass
            st_space("v", "3vh")
            with st_grid(cols=cols, gap="5vh 0.5vw", cell_styles=cells) as g:
                for before, key, after in _WATCH:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body, before, (bs.keyword, key), after, tag=t.div)
                    with g.cell():
                        pass  # right margin
