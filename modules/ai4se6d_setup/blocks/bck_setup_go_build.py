"""Slide — Go build: fresh folder, git init, opencode; commit when something works."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Go build slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    caption = s.project.titles.caption
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_START = (
    "mkdir -p ~/ai4se/freeselfapp\n"
    "cd ~/ai4se/freeselfapp\n"
    "git init\n"
    "opencode"
)
_SAVE = 'git add -A && git commit -m "it works"'


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Go Build", tag=t.div, toc_lvl="1")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_START, language="bash", line_numbers=False)
        st_write(bs.body, "Paste your first prompt, then iterate.")
        st_write(bs.body, (bs.label, "It works? Save it (2nd terminal):"))
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_SAVE, language="bash", line_numbers=False)
        st_write(bs.caption, "git = save points you can come back to. We learn it properly tomorrow.", tag=t.div)
