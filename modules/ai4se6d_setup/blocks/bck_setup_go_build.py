"""Slide — Go build: fresh folder, git init, opencode; commit when something works."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Go build slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    caption = s.project.titles.caption
bs = BlockStyles

_CODE_ZOOM = 220  # st_code font_size is not applied by Pygments: zoom instead
_START = (
    "mkdir -p ~/ai4se/freeselfapp\n"
    "cd ~/ai4se/freeselfapp\n"
    "git init\n"
    "opencode"
)
_SAVE = 'git add -A && git commit -m "it works"'

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Everyone creates ~/ai4se/freeselfapp, runs git init and opencode, "
     "pastes a first prompt and starts iterating now."),
    ("The message",
     "Start the workshop: a fresh folder ~/ai4se/freeselfapp, git init, then opencode inside it. Paste the first "
     "prompt and iterate."),
    ("Why a fresh folder",
     "The agent reads and writes the folder it is started in: an empty project folder keeps it away from "
     "everything else on the machine."),
    ("Why git now",
     "« It works? Save it »: one commit in a 2nd terminal gives a save point to come back to if the next prompt "
     "breaks the app. The exercise sheet asks for 2+ commits."),
    ("Keep it light",
     "No git lesson today: two commands are enough. « We learn it properly tomorrow » (day 2 starts with git)."),
    ("Ask the room",
     "« Who has already lost working code after one change too many? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Go Build", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Go Build", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # Outer 5 % margins; commands stay copyable code boxes (NG, 2026-11-23)
        with st_grid(cols="5% 90% 5%", cell_styles=s.project.containers.row_cell_left) as g:
            with g.cell():
                pass
            with g.cell():
                with st_zoom(_CODE_ZOOM):
                    st_code(s.none, code=_START, language="bash", line_numbers=False)
                st_space("v", "3vh")
                with st_zoom(110):
                    st_write(bs.body, "Paste your first prompt, then iterate.", tag=t.div)
                    st_space("v", "2vh")
                    st_write(bs.body, (bs.label, "It works? Save it (2nd terminal):"), tag=t.div)
                with st_zoom(_CODE_ZOOM):
                    st_code(s.none, code=_SAVE, language="bash", line_numbers=False)
                st_space("v", "3vh")
                with st_zoom(110):
                    st_write(bs.caption, "git = save points you can come back to. We learn it properly tomorrow.",
                             tag=t.div)
            with g.cell():
                pass
