"""Slide — Installation step 0b: git and curl (and Homebrew on macOS), needed from step 1 on (NG « ok », 2026-11-26).

curl runs the installers of steps 1, 2 and 5; git clones the kit at step 4; brew installs Node (step 2) and gh
(step 6) on macOS. Before this slide no step installed them: Ubuntu desktops often lack git, and a fresh Mac has no
git until the Command Line Tools are installed (the Homebrew installer installs them).
No « Or ask opencode » line: opencode is installed at step 1, after this one.
"""
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
# One box per environment, always Windows, Ubuntu, macOS last (NG, 2026-11-24: learners copy the wrong lines)
_CHECK = "# check first — every system (macOS: brew --version too)\ngit --version && curl --version"
_WIN_UBUNTU = "# Windows (WSL) | Ubuntu\nsudo apt-get update && sudo apt-get install -y git curl"
# Homebrew: official one-line installer (brew.sh). It installs the Command Line Tools (git included) when missing.
_MACOS_BREW = ('# macOS — Homebrew (it also installs git)\n'
               '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
# Apple Silicon: brew lands in /opt/homebrew, not on the PATH — the two lines the installer prints as « Next steps ».
_MACOS_PATH = ("# macOS, when it has finished — put brew on the PATH (Apple M1 or later)\n"
               "echo 'eval \"$(/opt/homebrew/bin/brew shellenv)\"' >> ~/.zprofile\n"
               'eval "$(/opt/homebrew/bin/brew shellenv)"')

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 0b of the installation: everyone runs the check; those with a "
     "missing tool install it now; the others skip to step 1."),
    ("The message",
     "Two basic tools the next steps use: curl downloads the installers (steps 1, 2, 5), git copies the course kit "
     "(step 4). On macOS, Homebrew installs Node (step 2) and gh (step 6)."),
    ("Already done?",
     "git and curl both print a version (macOS: brew --version too): skip to step 1."),
    ("Per system",
     "Windows (WSL): the Ubuntu of WSL usually has both: the check passes. Ubuntu desktop: git is often missing. "
     "macOS: curl is there; git comes with the Command Line Tools — typing git without them opens an "
     "« install the tools? » window. Homebrew installs them for you."),
    ("The trap",
     "macOS: the Homebrew installer asks for your password and to press Enter, and may take 5-10 min (Command Line "
     "Tools). Paste the PATH box only when it has finished, not while it runs. Intel Mac: skip the PATH box "
     "(brew is in /usr/local/bin, already on the PATH)."),
    ("The check",
     "git --version and curl --version each print a version; macOS: brew --version too."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git --version && curl --version",
     "Each prints its version (e.g. git version 2.43.0). && runs the second only if the first succeeded: « command "
     "not found » (or a macOS window offering the tools) = that tool is missing, install it with your box."),
    ("Command — sudo apt-get update && sudo apt-get install -y git curl",
     "sudo = run as administrator: it asks YOUR password (nothing shows while you type: normal). apt-get update = "
     "refresh the list of available packages; install -y git curl = install both, answering « yes » to the "
     "question. Already installed? apt-get says so and changes nothing."),
    ("Command — /bin/bash -c \"$(curl -fsSL …/install.sh)\"",
     "Homebrew's official installer (brew.sh): curl downloads the script (-f fail on error, -s silent, -S show "
     "errors, -L follow redirects), $( … ) hands its text to bash -c, which runs it. It explains what it will do, "
     "asks for your password and Enter, installs the Command Line Tools if missing (git included), then Homebrew."),
    ("Command — echo 'eval \"$(/opt/homebrew/bin/brew shellenv)\"' >> ~/.zprofile",
     "Adds one line to ~/.zprofile, the file zsh reads when a terminal opens: every new terminal will find brew. "
     ">> = append to the end of the file (> would erase it)."),
    ("Command — eval \"$(/opt/homebrew/bin/brew shellenv)\"",
     "Does the same now, in THIS terminal: brew shellenv prints the PATH settings, eval applies them. No new "
     "terminal needed. Same two lines as the installer prints under « Next steps »."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.step, "Installation · step 0b of 8 · ~5 min", tag=t.div)
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "0b · git and curl", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — 0b · git and curl", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(130):
            st_write(bs.caption, "The next steps need them. Both print a version (macOS: brew too)? Skip to step 1.",
                     tag=t.div)
        st_space("v", "2vh")
        for box in (_CHECK, _WIN_UBUNTU, _MACOS_BREW, _MACOS_PATH):
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=box, language="bash", line_numbers=False)
            st_space("v", "1vh")
        st_space("v", "1vh")
        with st_zoom(115), st_block(bs.done_box):
            st_write(bs.body, (bs.done_label, "Done when: "), "every check prints a version.")
