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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — mkdir -p ~/ai4se/freeselfapp",
     "mkdir = make directory (create a folder). -p = also create missing parent folders, no error if it already "
     "exists. ~ = your home folder."),
    ("Command — cd ~/ai4se/freeselfapp",
     "cd = change directory: the terminal now works inside the new folder; the next commands act there."),
    ("Command — git init",
     "Turns the current folder into a git repository: creates a hidden .git folder that will hold all the save "
     "points. It saves nothing yet. Prints « Initialized empty Git repository in … ». The first branch is « main » "
     "(set in step 6)."),
    ("Command — opencode",
     "Without arguments, starts the agent's full-screen window in the current folder: it reads and writes this "
     "folder. Paste the first prompt at the bottom, Enter to send. Shift+Tab switches between build (edits files, "
     "runs commands) and plan (explores and proposes, does not edit project files). Leave with /exit or Ctrl+C."),
    ("Command — git add -A",
     "Prepares the next save point: puts every change of the folder (new, modified and deleted files) into the "
     "« staging area » (the list of what the next commit will contain). -A = all. Run it in a 2nd terminal, in "
     "~/ai4se/freeselfapp (cd there first)."),
    ("Symbol — &&",
     "Runs git commit only if git add succeeded."),
    ("Command — git commit -m \"it works\"",
     "Records a commit: a save point of the staged files, with your name, the date and a message. -m = the message "
     "follows, in quotes; write what works, e.g. \"v1: list and add\". « nothing to commit » = no change since the "
     "last commit. « Please tell me who you are » = step 6 not done."),
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
