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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — curl -fsSL https://opencode.ai/v2/install | bash",
     "curl downloads a file from a web address. -f = fail on a server error instead of passing an error page on, "
     "-s = silent (no progress bar), -S = still show an error if one happens, -L = follow a redirect to the new "
     "address. The downloaded file is the official install script of opencode 2 (checked on opencode.ai/docs). "
     "It installs opencode in your home folder: no sudo, no password."),
    ("Symbol — | (pipe)",
     "Sends the output of the command on its left as input to the command on its right. Here the script downloaded "
     "by curl is handed straight to bash, which runs it. Only do this with addresses you trust."),
    ("Command — npm install -g @opencode/cli",
     "npm is the package installer that comes with Node.js. install = download and install a package; -g = "
     "« global »: a command usable from any folder, not a library for one project. @opencode/cli is the official "
     "package name of opencode 2 (opencode.ai/docs). Needs Node first (step 2); a « permission denied » error means "
     "Node was installed without nvm: use the curl line instead."),
    ("Command — brew install anomalyco/tap/opencode-v2",
     "brew (Homebrew) is the usual installer of command-line tools on macOS. anomalyco/tap = the publisher's own "
     "catalogue (a « tap »), opencode-v2 = the package in it. Official line from opencode.ai/docs. No Homebrew yet? "
     "Use the curl line."),
    ("Command — exec $SHELL",
     "Replaces the current shell by a fresh copy of itself, in the same window: it re-reads its start-up file "
     "(~/.bashrc or ~/.zshrc), where the installer added opencode's folder to the PATH (the list of folders where "
     "the terminal looks for commands). Same effect as closing and reopening the terminal. Nothing is lost except "
     "the variables set by hand in this terminal."),
    ("Command — opencode --version",
     "Asks opencode to print its version number and stop (it does not open the agent). --version = an option "
     "written with two dashes, a full word. Expected: 2.x.y."),
    ("Symbol — # Windows (WSL) | Ubuntu | macOS",
     "The first line of each box is a comment (starts with #): it says which system the box is for and does not run. "
     "Here the | is plain text, not a pipe, because it is inside the comment."),
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
