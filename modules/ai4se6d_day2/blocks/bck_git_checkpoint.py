"""Slide — Pattern 2: checkpoint commits."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Checkpoint styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    quote = Style.create(s.project.titles.subtitle + s.center_txt, "gitcp_quote")
bs = BlockStyles

_CHECKPOINT = """\
git add <files> && git commit -m "chore: checkpoint before refactor"
# ... let the agent work ...
git diff          # happy? test and commit.   not happy?
git restore .     # back to the checkpoint (uncommitted work is lost)"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "2 · Checkpoint Commits", tag=t.div, toc_lvl="+1")
        st_write(bs.quote, "Save the game before the boss fight.", tag=t.div)
        st_space("v", 1)
        st_code(s.none, code=_CHECKPOINT, language="bash", line_numbers=False, font_size="24pt")
        st_space("v", 1)
        st_write(
            bs.body, (bs.label, "Use it before: "),
            "a big refactor, an approach you doubt, a multi-file change.", tag=t.div,
        )
