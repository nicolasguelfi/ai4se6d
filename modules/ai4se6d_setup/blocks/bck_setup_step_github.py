"""Slide — Installation step 6a: GitHub account, gh CLI, gh auth login."""
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
    caption = s.project.titles.caption
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "setup_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "setup_done_label")
bs = BlockStyles

_CODE_ZOOM = 118  # st_code font_size is not applied by Pygments: zoom instead
# One box per environment, always Windows, Ubuntu, macOS last (NG, 2026-11-24: learners copy the wrong lines)
_GH_WIN_UBUNTU = "# Windows (WSL) | Ubuntu\nsudo apt install gh"
_GH_MACOS = "# macOS\nbrew install gh"
_GH_LOGIN = "# then, every system:\ngh auth login           # GitHub.com, HTTPS, browser"

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 6 of the installation, first half: everyone logs in with gh "
     "auth login; wait until gh auth status says « Logged in »."),
    ("The message",
     "A GitHub account and the gh command line, logged in: git can then push without asking for a password."),
    ("No account yet",
     "github.com/signup — a personal account is fine."),
    ("The login",
     "gh auth login: choose GitHub.com, HTTPS, and log in with the browser."),
    ("No browser",
     "In WSL or the VM: copy the one-time code, open github.com/login/device yourself in ANY browser (even on your "
     "own computer) and type the code."),
    ("Ubuntu: Firefox messages",
     "On Ubuntu, gh opens Firefox, a snap: it prints many « update.go:193: cannot change mount namespace … » lines "
     "and Gtk / Glycin messages. They are harmless: do NOT press Ctrl+C (it kills gh and Firefox, the login is "
     "lost). Wait, or enter the code at github.com/login/device from any browser."),
    ("The trap and the check",
     "« git asks for a password » = not logged in: redo this step. Done when gh auth status says « Logged in »."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 6 of 8 · ~10 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "6 · GitHub Login", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 6 · GitHub Login", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(bs.body, (bs.label, "No account? "), (bs.cmd, "github.com/signup"), " (personal is fine)")
        st_space("v", "2vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GH_WIN_UBUNTU, language="bash", line_numbers=False)
        st_space("v", "1.5vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GH_MACOS, language="bash", line_numbers=False)
        st_space("v", "1.5vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_GH_LOGIN, language="bash", line_numbers=False)
        st_space("v", "2vh")
        with st_zoom(115), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), (bs.cmd, "gh auth status"), " says “Logged in”.")
        st_space("v", "2vh")
        with st_zoom(105):
            st_write(bs.caption, "Ubuntu: « update.go … mount namespace » lines are harmless (Firefox snap): "
                     "no Ctrl+C. No browser? Type the code at github.com/login/device, any browser.", tag=t.div)
