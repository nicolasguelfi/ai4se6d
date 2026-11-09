"""Slide — Installation step 5a: GitHub account, gh CLI, gh auth login."""
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
    caption = s.project.titles.caption
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_GH = (
    "brew install gh         # macOS\n"
    "sudo apt install gh     # Linux / WSL\n"
    "gh auth login           # GitHub.com, HTTPS, browser"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 5 of 7 · ~10 min", tag=t.div)
        st_write(bs.heading, "5 · GitHub Login", tag=t.div, toc_lvl="1")
        with st_zoom(85):
            st_write(bs.body, (bs.label, "No account? "), (bs.cmd, "github.com/signup"), " (personal is fine)")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GH, language="bash", line_numbers=False)
        with st_zoom(85), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "gh auth status"), " says “Logged in”.")
        st_write(bs.caption, "No browser (WSL, VM)? Copy the code, open the link yourself.", tag=t.div)
