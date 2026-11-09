"""Slide — Installation step 5b: tell git who you are (global name and email)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 220  # st_code font_size is not applied by Pygments: zoom instead
_GIT = (
    'git config --global user.name  "Your Name"\n'
    'git config --global user.email "you@example.com"\n'
    "git config --global init.defaultBranch main"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 5 of 7 · ~5 min", tag=t.div)
        st_write(bs.heading, "5 · Your Git Identity", tag=t.div, toc_lvl="1")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GIT, language="bash", line_numbers=False)
        with st_zoom(85):
            st_write(bs.body, (bs.label, "Email: "), "the one of your GitHub account.")
            with st_block(bs.done_box):
                st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "git config --global --list"), " shows them.")
