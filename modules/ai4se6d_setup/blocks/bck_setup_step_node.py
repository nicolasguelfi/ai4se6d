"""Slide — Installation step 2: install Node.js 20+ (LTS), needed for day 2 (npm)."""
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

_CODE_ZOOM = 118  # st_code font_size is not applied by Pygments: zoom instead
# nvm = the installer recommended on nodejs.org/en/download (v0.41.0 checked 2026-11-09).
# One box per environment, always Windows, Ubuntu, macOS last (NG, 2026-11-24: learners copy the wrong lines)
_WIN_UBUNTU = (
    "# Windows (WSL) | Ubuntu — nvm\n"
    "sudo apt-get install -y libatomic1\n"
    "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh | bash\n"
    '. "$HOME/.nvm/nvm.sh"          # load nvm in this terminal\n'
    "nvm install --lts"
)
_MACOS = "# macOS\nbrew install node"
_CHECK = "# check — every system\nnode --version && npm --version"

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 2 of the installation: those without Node v20+ install it "
     "now (needed tomorrow for CalcApp); the others skip to step 3."),
    ("The message",
     "Node.js is not needed this afternoon: it runs CalcApp tomorrow (npm). Installing it now saves time tomorrow."),
    ("Already done?",
     "node --version shows v20 or more: skip to step 3."),
    ("Two ways",
     "macOS: Homebrew. Otherwise nvm, the installer recommended on nodejs.org (v0.41.0, checked on 2026-11-09), "
     "then nvm install --lts after loading nvm in the same terminal (. \"$HOME/.nvm/nvm.sh\", as nvm's README "
     "gives): no new terminal. Ubuntu also needs libatomic1 (minimal Ubuntu: « libatomic.so.1: cannot open shared "
     "object file »). brew needs nothing else."),
    ("The trap",
     "« node missing, or older than v20 »: redo this step (see Common Errors)."),
    ("The check",
     "node shows v20 or more, and npm prints a version."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 2 of 8 · ~5 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "2 · Node.js (LTS)", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 2 · Node.js (LTS)", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(130):
            st_write(bs.caption, "Needed tomorrow to run CalcApp (npm). Already ≥ 20? Skip to step 3.", tag=t.div)
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_WIN_UBUNTU, language="bash", line_numbers=False)
        st_space("v", "1.5vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_MACOS, language="bash", line_numbers=False)
        st_space("v", "1.5vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_CHECK, language="bash", line_numbers=False)
        st_space("v", "2vh")
        with st_zoom(115), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "node shows ", (bs.cmd, "v20"), " or more, npm a version.")
