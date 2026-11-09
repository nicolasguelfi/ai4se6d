"""Slide — Installation step 4: install GSE-One, pinned to v0.90.0 (after opencode)."""
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

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_FOLDER = "mkdir -p ~/ai4se/gse-check && cd ~/ai4se/gse-check"
_GSE = (
    "curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/gensem/v0.90.0/install.sh"
    " | GSE_PLATFORM=opencode GSE_VERSION=v0.90.0 sh"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 4 of 7 · ~10 min", tag=t.div)
        st_write(bs.heading, "4 · GSE-One v0.90.0", tag=t.div, toc_lvl="1")
        st_write(bs.caption, "Needs opencode 2 (step 1). Installs into this test folder.", tag=t.div)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_FOLDER, language="bash", line_numbers=False)
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GSE, language="bash", line_numbers=False)
        with st_zoom(85), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "cat .gse/registry"), " prints ", (bs.cmd, ".opencode"))

