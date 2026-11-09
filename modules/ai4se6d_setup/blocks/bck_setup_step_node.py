"""Slide — Installation step 2: install Node.js 20+ (LTS), needed for day 2 (npm)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Installation step slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    step = Style.create(s.project.titles.caption + s.center_txt, "setup_step_caption")
    body = s.project.titles.body
    caption = s.project.titles.caption
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 150  # st_code font_size is not applied by Pygments: zoom instead
# nvm = the installer recommended on nodejs.org/en/download (v0.41.0 checked 2026-11-09).
_INSTALL = (
    "brew install node        # macOS, or:\n"
    "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh | bash"
)
_LTS = "# open a NEW terminal, then:\nnvm install --lts         # skip if you used brew"
_CHECK = "node --version && npm --version"


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.none):
            st_write(bs.step, "Installation · step 2 of 8 · ~5 min", tag=t.div)
            st_write(bs.heading, "2 · Node.js (LTS)", tag=t.div, toc_lvl="1")
            st_write(bs.caption, "Needed tomorrow to run CalcApp (npm). Already ≥ 20? Skip to step 3.", tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_INSTALL, language="bash", line_numbers=False)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_LTS + "\n" + _CHECK, language="bash", line_numbers=False)
        with st_zoom(85), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "node shows ", (bs.cmd, "v20"), " or more, npm a version.")
