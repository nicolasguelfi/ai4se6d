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

_COMMANDS = """\
git status                  # what changed? run it all the time
git diff                    # the exact lines: your review tool
git add <file>              # stage what you have reviewed
git commit -m "feat: ..."   # snapshot with a message
git log --oneline           # the timeline
git restore <file>          # throw an unwanted change away"""


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Explain the six commands; learners run all six in the Git exercise a few"
     " slides later."),
    ("The message",
     "Six commands cover the whole day: status, diff, add, commit, log, restore."),
    ("See",
     "git status tells what changed — run it all the time; git diff shows the exact lines: it is the review tool."),
    ("Save",
     "git add <file> stages what you have reviewed; git commit -m \"feat: ...\" takes the snapshot with a message; "
     "git log --oneline shows the timeline."),
    ("Undo",
     "git restore <file> throws an unwanted change away."),
    ("The trap",
     "After the agent worked: never git add . without reading the diff."),
    ("Ask the room",
     "« Which of the six have you never used? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "Six Commands for Today", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Six Commands for Today", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "12vh")
        with st_zoom(125):
            st_code(s.none, code=_COMMANDS, language="bash", line_numbers=False, font_size="28pt")
        st_space("v", "12vh")
        with st_zoom(120):
            st_write(bs.warning, "After the agent worked: never git add . without reading the diff.", tag=t.div)
