"""Slide — Pattern 2: checkpoint commits."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Checkpoint styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    quote = Style.create(s.project.titles.subtitle + s.center_txt, "gitcp_quote")
bs = BlockStyles

_CODE_ZOOM = 132  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_CHECKPOINT = """\
git add -A && git commit -m "chore: checkpoint before refactor"
# ... let the agent work ...
git diff          # happy? test and commit.   not happy?
git restore .     # back to the checkpoint (uncommitted work is lost)"""


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Explain the checkpoint pattern; learners do the break-then-restore part "
     "in the Git exercise."),
    ("The message",
     "Second habit: commit a checkpoint before letting the agent attempt something risky — « save the game before "
     "the boss fight »."),
    ("How",
     "Commit the current state, let the agent work, read git diff. Happy: test and commit. Not happy: git restore . "
     "brings back the checkpoint."),
    ("When",
     "Before a big refactor, an approach you doubt, or a change across several files."),
    ("The trap",
     "git restore . discards every uncommitted change: anything not in the checkpoint is lost."),
    ("Link to GSE-One",
     "GSE-One applies the same idea with a safety tag gse-backup/… before a risky operation."),
    ("Ask the room",
     "« Which change of yesterday would have deserved a checkpoint? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git add -A",
     "Stages every change of the project: modified, new and deleted files. -A = --all. Fine here because you save "
     "the state you already trust, before the agent works."),
    ("Symbol — &&",
     "Runs the next command only if the previous one succeeded: no commit if git add failed."),
    ("Command — git commit -m \"chore: checkpoint before refactor\"",
     "Saves the staged state as a commit: that commit is the checkpoint. -m = the message, in quotes. « chore: » ="
     " type for housekeeping work that adds no feature."),
    ("Command — git diff",
     "After the agent worked: shows every line changed since the checkpoint (- removed, + added). q to quit the "
     "viewer."),
    ("Command — git restore .",
     "Throws away all uncommitted changes to tracked files in this folder and below (the dot): the files go back "
     "to the checkpoint. No undo. Trap: new files the agent created are not removed — git status lists them as "
     "untracked; delete them by hand (or git clean -n to list, git clean -f to delete)."),
    ("Symbol — #",
     "Starts a comment: the shell ignores the rest of the line. Not typed."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "2 · Checkpoint Commits", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Checkpoint Commits", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(120):
            st_write(bs.quote, "Save the game before the boss fight.", tag=t.div)
        st_space("v", "9vh")
        with st_zoom(120):
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_CHECKPOINT, language="bash", line_numbers=False, font_size="24pt")
        st_space("v", "9vh")
        with st_zoom(120):
            st_write(
                bs.body, (bs.label, "Use it before: "),
                "a big refactor, an approach you doubt, a multi-file change.", tag=t.div,
            )
