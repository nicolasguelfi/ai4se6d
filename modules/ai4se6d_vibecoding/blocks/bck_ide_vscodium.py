"""Act IV — VSCodium: the recommended editor, install and switch its AI off (NG, 2026-11-22).

Text only: the screenshot has its own slide right after (bck_ide_vscodium_capture) — NG, 2026-11-22:
a screenshot and text on the same slide are unreadable in a room over 3 m long.
"""
# Source: ai4se-kit/syllabus/ide-guide.md (kit 2026-11-22.3); chat.disableAIFeatures checked in VSCodium 1.112.
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """VSCodium slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    caption = Style.create(s.project.titles.caption + s.center_txt, "ide_vscodium_caption")
    body = s.project.titles.body
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    cmd = Style.create(
        s.project.titles.body + s.text.fonts.font_monospace + s.project.colors.accent, "ide_vscodium_cmd",
    )
    box = s.project.containers.callout
bs = BlockStyles

_CODE_ZOOM = 120  # st_code font_size is not applied by Pygments: zoom instead
# One box per environment, always Windows, Ubuntu, macOS last (NG, 2026-11-24: learners copy the wrong lines)
_INSTALL_BOXES = [
    "# Windows\nwinget install VSCodium.VSCodium",
    "# Ubuntu\nsudo snap install codium --classic",
    "# macOS\nbrew install --cask vscodium",
]
_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to install now. VSCodium is the course editor: learners install it this afternoon "
     "after the 8 installation steps if time allows, at the latest tomorrow morning before the first exercise, and "
     "switch its AI off. In the course VM it is VS Code, already installed, AI already off."),
    ("The message",
     "VSCodium is the course editor: the open-source build of VS Code — free, no Copilot "
     "account, no Microsoft telemetry."),
    ("Install",
     "One command per system: brew (macOS), winget (Windows), snap (Ubuntu: snap is there by default; the "
     "VSCodium snap needs --classic and sudo). Other Linux: flatpak install flathub com.vscodium.codium "
     "(flatpak must be installed first). Commands from vscodium.com, Install section."),
    ("Once: switch its AI off",
     "Settings → disable AI features (chat.disableAIFeatures: true). In the workshops opencode is the only agent: a "
     "second agent in the editor would overwrite its work (previous slide)."),
    ("Open your project",
     "cd ~/ai4se/calcapp then codium . (in the course VM: code .). Windows: Start menu → VSCodium → File → Open "
     "Folder; for a WSL project, \\\\wsl$\\Ubuntu\\home\\…\\ai4se\\calcapp."),
    ("What it is for",
     "Reading the code and the agent's changes — the next slide shows the Source Control diff."),
    ("Mini guide",
     "ai4se-kit/syllabus/ide-guide.md in the course kit; its twin for opencode 2: syllabus/opencode-guide.md (mini "
     "guide + cheat sheet)."),
    ("Ask the room",
     "« Who already has VS Code? What would you have to switch off in it to follow the same rule? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Symbol — # Windows / # Ubuntu / # macOS",
     "A comment line: it only says which system the box is for. Type only the line under it, in that system's "
     "terminal."),
    ("Command — winget install VSCodium.VSCodium",
     "winget = Windows' own package manager (a program that downloads and installs other programs), already "
     "present on Windows 10 and 11. Type it in PowerShell or the Terminal app, not in WSL. install = the action; "
     "VSCodium.VSCodium = the package's exact identifier (publisher.name), so winget cannot pick a look-alike. "
     "Windows may ask to confirm (administrator prompt) and winget may ask to accept the source's terms: answer Y."),
    ("Command — sudo snap install codium --classic",
     "snap = Ubuntu's package manager for applications (the Snap Store), there by default. sudo = run the command "
     "as administrator: it asks for YOUR password (nothing shows while you type, that is normal). install codium "
     "= install the package named codium (VSCodium's name in the Snap Store). --classic = let the application see "
     "your whole disk like an ordinary program, outside the snap sandbox; an editor needs it to open your project "
     "folders, and snap refuses to install it without that flag."),
    ("Command — brew install --cask vscodium",
     "brew = Homebrew, the usual package manager on macOS; it must be installed first (brew.sh). install vscodium "
     "= install the package vscodium. --cask = the package is a graphical application (it lands in Applications), "
     "not a command-line tool. No sudo with brew."),
    ("Setting — chat.disableAIFeatures: true",
     "A setting, not a terminal command. Open Settings (Cmd+, on macOS, Ctrl+, elsewhere), type disable AI "
     "features in the search box, tick the box. It hides and turns off the editor's chat, its inline suggestions "
     "(completion) and the Copilot extension. chat.disableAIFeatures is its internal name; true = on. In the "
     "settings.json file the same line reads \"chat.disableAIFeatures\": true. Set it at user level (all your "
     "projects)."),
    ("Command — codium . (course VM: code .)",
     "Opens the editor on a folder. codium = the command that starts VSCodium from the terminal (code for VS "
     "Code); . (dot) = the current folder, so run cd ~/ai4se/calcapp first. If the terminal answers « command not "
     "found », open the folder from the editor's File → Open Folder instead."),
    ("Text — ai4se-kit/syllabus/ide-guide.md",
     "Not a command: the path of the mini guide in the course kit (file ide-guide.md, folder syllabus, inside "
     "ai4se-kit — on disk ~/ai4se/ai4se-kit). On the slide it is a link to the same file on GitHub."),
]
_GUIDE_URL = "https://github.com/nicolasguelfi/ai4se-kit/blob/main/syllabus/ide-guide.md"


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "VSCodium", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — VSCodium", entries=_NOTES, position="left", width="50vw")
        st_space("v", "2vh")
        with st_zoom(105):
            st_write(
                bs.caption,
                "The course editor (VM: VS Code). Install it today if time allows, at the latest tomorrow morning.",
                tag=t.div,
            )
        st_space("v", "1.5vh")
        for box in _INSTALL_BOXES:
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=box, language="bash", line_numbers=False)
            st_space("v", "1vh")
        st_space("v", "1.5vh")
        with st_zoom(110), st_block(bs.box):
            st_write(
                bs.body, (bs.keyword_warn, "Once: "), "Settings → ",
                (bs.keyword_accent, "disable AI features"),
                tag=t.div,
            )
            st_write(bs.cmd, "chat.disableAIFeatures: true", tag=t.div)
        st_space("v", "1.5vh")
        with st_zoom(110), st_block(s.center_txt):
            st_write(bs.body, "Mini guide in the course kit:", tag=t.div)
            st_write(bs.cmd, "ai4se-kit/syllabus/ide-guide.md", link=_GUIDE_URL, tag=t.div)
