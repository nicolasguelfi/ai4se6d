"""Slide — The six Git commands of the day."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Command list styles."""
    heading = s.project.titles.heading
    warning = Style.create(s.project.titles.body + s.project.colors.critical + s.bold + s.center_txt, "gitcmd_warn")
bs = BlockStyles

_CODE_ZOOM = 107  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_COMMANDS = """\
git status                  # what changed? run it all the time
git diff                    # the exact lines: your review tool
git add src/App.tsx         # one file, e.g.: stage what you reviewed
git commit -m "feat: ..."   # snapshot with a message
git log --oneline           # the timeline
git restore src/App.tsx     # throw an unwanted change away"""


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Explain the six commands; learners run all six in the Git exercise a few"
     " slides later."),
    ("The message",
     "Six commands cover the whole day: status, diff, add, commit, log, restore."),
    ("See",
     "git status tells what changed — run it all the time; git diff shows the exact lines: it is the review tool."),
    ("Save",
     "git add src/App.tsx (one file, e.g.) stages what you have reviewed; git commit -m \"feat: ...\" takes the snapshot with a message; "
     "git log --oneline shows the timeline."),
    ("Undo",
     "git restore src/App.tsx throws an unwanted change away."),
    ("The trap",
     "After the agent worked: never git add . without reading the diff."),
    ("Ask the room",
     "« Which of the six have you never used? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git status",
     "Lists the files that changed: « Changes to be committed » (staged, green), « Changes not staged » (modified,"
     " red) and « Untracked files » (new files Git does not follow yet). It changes nothing: run it as often as "
     "you like. « nothing to commit, working tree clean » = everything is committed."),
    ("Command — git diff",
     "Shows, line by line, what changed in your files since the last commit and that is not staged yet: lines "
     "starting with - (red) were removed, lines with + (green) were added. Nothing is modified. Long output opens "
     "in a viewer: arrows to scroll, q to quit. Trap: a brand-new file (« untracked ») does not appear."),
    ("Command — git add src/App.tsx",
     "Puts the current content of that file into the staging area: it will be part of the next commit. Argument = "
     "the file to stage (path from the project folder); you can list several files. Edit the file again after git "
     "add? Run git add again, or the new edit is not included."),
    ("Command — git commit -m \"feat: ...\"",
     "Saves the staged changes as one commit (a snapshot). -m = the message follows, in quotes so that several "
     "words stay one argument. « feat: » = the type of change (see the conventions slide). The first commit may "
     "ask who you are: git config --global user.name / user.email."),
    ("Command — git log --oneline",
     "Shows the history of the current branch, newest commit first. --oneline = one line per commit: a short id (7"
     " characters, e.g. a1b2c3d) then the first line of the message. Long output opens in a viewer: q to quit."),
    ("Command — git restore src/App.tsx",
     "Throws away the uncommitted changes of that file: it goes back to its last committed (or staged) version. "
     "Argument = the file (path from the project folder). No undo: the discarded lines are gone. Only for files "
     "Git already tracks — a new file is not removed."),
    ("Symbol — #",
     "Starts a comment: the shell ignores everything after it on the line. The comments on the slide are "
     "explanations, you do not type them."),
    ("Symbol — . in git add .",
     "The dot means « the current folder and everything inside »: git add . stages every change, including the "
     "ones you never read."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Six Commands for Today", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Six Commands for Today", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "12vh")
        with st_zoom(120):
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_COMMANDS, language="bash", line_numbers=False, font_size="28pt")
        st_space("v", "12vh")
        with st_zoom(120):
            st_write(bs.warning, "After the agent worked: never git add . without reading the diff.", tag=t.div)
