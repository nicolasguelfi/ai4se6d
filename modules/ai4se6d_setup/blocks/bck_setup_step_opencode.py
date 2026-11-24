"""Slide — Installation step 1: install opencode 2 and check its version."""
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
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    warn = Style.create(s.bold + s.project.colors.highlight, "setup_warn")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
# Verified on opencode.ai/docs (V2 = latest) on 2026-11-09.
# One box per environment, always Windows, Ubuntu, macOS last (NG, 2026-11-24: learners copy the wrong lines)
_INSTALL = "# Windows (WSL) | Ubuntu | macOS\ncurl -fsSL https://opencode.ai/v2/install | bash"
_ALT_NPM = "# or, any system with Node:\nnpm install -g @opencode/cli"
_ALT_MACOS = "# or, macOS only:\nbrew install anomalyco/tap/opencode-v2"

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 1 of the installation: everyone runs one install command, "
     "checks opencode --version prints 2.x.y; only on « command not found », exec $SHELL reloads the terminal."),
    ("The message",
     "opencode 2 is the coding agent of the week: one install command, then a version check."),
    ("Three ways",
     "The official install script (checked on opencode.ai/docs on 2026-11-09); on macOS, Homebrew as an "
     "alternative; npm if you already use Node."),
    ("The trap",
     "The install script adds opencode to your PATH, but the open terminal does not see it: « command not "
     "found » means « reload it: exec $SHELL ». Homebrew and npm installs usually work at once (see Common Errors)."),
    ("The check",
     "opencode --version prints 2.x.y (e.g. 2.2.6). A 1.x version is not the one of the course."),
    ("Link to the next steps",
     "Step 3 connects your model key to opencode; step 5 (GSE-One) needs opencode 2 installed first."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 1 of 8 · ~10 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "1 · Install opencode 2", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 1 · Install opencode 2", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_INSTALL, language="bash", line_numbers=False)
        st_space("v", "2vh")
        with st_grid(cols="1fr 1fr", gap="2vw") as g:
            with g.cell(), st_zoom(125):
                st_code(s.none, code=_ALT_NPM, language="bash", line_numbers=False)
            with g.cell(), st_zoom(125):
                st_code(s.none, code=_ALT_MACOS, language="bash", line_numbers=False)
        st_space("v", "2vh")
        with st_zoom(120):
            st_write(bs.body, "Check — ", (bs.warn, "« command not found »?"), " reload it: ", (bs.cmd, "exec $SHELL"), ", then:")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code="opencode --version", language="bash", line_numbers=False)
        st_space("v", "2vh")
        with st_zoom(140), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "it prints ", (bs.cmd, "2.x.y"), " (e.g. 2.2.6).")
