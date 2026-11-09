"""Slide — Installation step 1: install opencode 2 and check its version."""
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
    warn = Style.create(s.bold + s.project.colors.highlight, "setup_warn")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
# Verified on opencode.ai/docs (V2 = latest) on 2026-11-09.
_INSTALL = "curl -fsSL https://opencode.ai/v2/install | bash"
_ALTERNATIVES = (
    "brew install anomalyco/tap/opencode-v2   # macOS, alternative\n"
    "npm install -g @opencode/cli             # if you already use Node"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 1 of 8 · ~10 min", tag=t.div)
        st_write(bs.heading, "1 · Install opencode 2", tag=t.div, toc_lvl="1")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_INSTALL, language="bash", line_numbers=False)
        with st_zoom(130):
            st_code(s.none, code=_ALTERNATIVES, language="bash", line_numbers=False)
        with st_zoom(85):
            st_write(bs.body, (bs.warn, "Open a NEW terminal"), ", then:")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="opencode --version", language="bash", line_numbers=False)
        with st_zoom(85), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "it prints ", (bs.cmd, "2.x.y"), " (e.g. 2.2.6).")
