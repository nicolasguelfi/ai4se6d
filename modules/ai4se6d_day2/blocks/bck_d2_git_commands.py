"""Slide — The six Git commands of the day."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Command list styles."""
    heading = s.project.titles.heading
    warning = Style.create(s.project.titles.body + s.project.colors.critical + s.bold + s.center_txt, "d2_gitcmd_warn")
bs = BlockStyles

_COMMANDS = """\
git status                  # what changed? run it all the time
git diff                    # the exact lines: your review tool
git add <file>              # stage what you have reviewed
git commit -m "feat: ..."   # snapshot with a message
git log --oneline           # the timeline
git restore <file>          # throw an unwanted change away"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Six Commands for Today", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        st_code(s.none, code=_COMMANDS, language="bash", line_numbers=False, font_size="28pt")
        st_space("v", 1)
        st_write(bs.warning, "After the agent worked: never git add . without reading the diff.", tag=t.div)
