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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — sudo apt-get install -y libatomic1",
     "sudo = run the command as administrator: it asks YOUR password (nothing shows while you type: normal). apt-get "
     "is Ubuntu's software installer (WSL runs Ubuntu too); install = add a package; -y = answer « yes » to the "
     "confirmation question. libatomic1 is a small system library that recent Node.js versions need; minimal Ubuntu "
     "images lack it. Already installed? apt-get says so and changes nothing."),
    ("Command — curl -o- (address of install.sh) | bash",
     "curl downloads nvm's official install script (version v0.41.0, from the nvm GitHub project); -o- = write the "
     "download to the screen output (- means « standard output ») instead of a file, so that | hands it to bash, "
     "which runs it. The script copies nvm into ~/.nvm and adds two loading lines to ~/.bashrc (or ~/.zshrc). nvm "
     "= Node Version Manager: installs Node in your home folder, no sudo needed."),
    ("Command — . \"$HOME/.nvm/nvm.sh\"",
     "The lone dot means « read this file and run it inside THIS terminal » (also written source). It loads the nvm "
     "command now, so no new terminal is needed. $HOME = your home folder (same as ~); the quotes keep the path in one "
     "piece even if it contains a space. The comment after # is ignored."),
    ("Command — nvm install --lts",
     "Downloads and installs the current Node.js LTS (Long-Term Support: the stable version, v20 or newer) with its "
     "npm, and switches to it. --lts = « the latest LTS » instead of a number. The first version nvm installs becomes "
     "the default in every new terminal."),
    ("Command — brew install node",
     "macOS: Homebrew installs the current Node.js and npm in one go. No Homebrew? Use nvm (the box above works on "
     "macOS too, without the sudo apt-get line)."),
    ("Command — node --version && npm --version",
     "Each prints its version: node must show v20 or more (e.g. v22.11.0), npm any number. && runs the second command "
     "only if the first succeeded: « node: command not found » stops there (then exec $SHELL, or redo the step)."),
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
