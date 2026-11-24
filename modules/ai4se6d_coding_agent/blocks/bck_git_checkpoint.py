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
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "2 · Checkpoint Commits", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Checkpoint Commits", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(115):
            st_write(bs.quote, "Save the game before the boss fight.", tag=t.div)
        st_space("v", "9vh")
        with st_zoom(125):
            st_code(s.none, code=_CHECKPOINT, language="bash", line_numbers=False, font_size="24pt")
        st_space("v", "9vh")
        with st_zoom(105):
            st_write(
                bs.body, (bs.label, "Use it before: "),
                "a big refactor, an approach you doubt, a multi-file change.", tag=t.div,
            )
