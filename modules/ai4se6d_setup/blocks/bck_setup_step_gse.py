"""Slide — Installation step 5: install GSE-One, pinned to v0.92.1 (after opencode)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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

_CODE_ZOOM = 140  # st_code font_size is not applied by Pygments: zoom instead
# One block (folder + pinned install), split with "\" so no line wraps on screen.
_GSE = (
    "mkdir -p ~/ai4se/gse-check && cd ~/ai4se/gse-check\n"
    "curl -fsSL https://raw.githubusercontent.com/nicolasguelfi/gensem/v0.92.1/install.sh \\\n"
    "  | GSE_PLATFORM=opencode GSE_VERSION=v0.92.1 sh"
)

_NOTES = [
    ("The message",
     "GSE-One is installed now, pinned to v0.92.1, so that everyone has the same version for the rest of the "
     "course."),
    ("Why a test folder",
     "GSE-One installs into a project folder: ~/ai4se/gse-check is only there to check that the install works."),
    ("Order matters",
     "It needs opencode 2 (step 1). « GSE-One before opencode 2 » is a common error: install opencode 2, then "
     "redo this step."),
    ("The check",
     "cat .gse/registry prints .opencode: GSE-One found opencode as its platform."),
    ("Ask the room",
     "« Whose registry prints something else? » — fix it now, before the workshop."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 5 of 8 · ~10 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "5 · GSE-One v0.92.1", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 5 · GSE-One v0.92.1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(140):
            st_write(bs.caption, "Needs opencode 2 (step 1). Installs into this test folder.", tag=t.div)
        st_space("v", "6vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GSE, language="bash", line_numbers=False)
        st_space("v", "7vh")
        with st_zoom(150), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "cat .gse/registry"), " prints ", (bs.cmd, ".opencode"))
