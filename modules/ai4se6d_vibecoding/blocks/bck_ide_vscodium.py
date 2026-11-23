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

_CODE_ZOOM = 190  # st_code font_size is not applied by Pygments: zoom instead
_INSTALL = (
    "brew install --cask vscodium                  # macOS\n"
    "winget install VSCodium.VSCodium              # Windows\n"
    "sudo snap install codium --classic            # Ubuntu"
)
_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to install now. VSCodium is optional (no installation step of the course needs an editor): learners who want it use these commands on their own and switch its AI off."),
    ("The message",
     "VSCodium is the recommended editor for the course: the open-source build of VS Code — free, no Copilot "
     "account, no Microsoft telemetry."),
    ("Install",
     "One command per system: brew (macOS), winget (Windows), snap (Ubuntu: snap is there by default; the "
     "VSCodium snap needs --classic and sudo). Other Linux: flatpak install flathub com.vscodium.codium "
     "(flatpak must be installed first). Commands from vscodium.com, Install section."),
    ("Once: switch its AI off",
     "Settings → disable AI features (chat.disableAIFeatures: true). In the workshops opencode is the only agent: a "
     "second agent in the editor would overwrite its work (previous slide)."),
    ("What it is for",
     "Reading the code and the agent's changes — the next slide shows the Source Control diff."),
    ("Mini guide",
     "ai4se-kit/syllabus/ide-guide.md in the course kit."),
    ("Ask the room",
     "« Who already has VS Code? What would you have to switch off in it to follow the same rule? »"),
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
                "The open-source build of VS Code: free, no Copilot account, no Microsoft telemetry.",
                tag=t.div,
            )
        st_space("v", "2.5vh")
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_INSTALL, language="bash", line_numbers=False)
        st_space("v", "2.5vh")
        with st_zoom(110), st_block(bs.box):
            st_write(
                bs.body, (bs.keyword_warn, "Once: "), "Settings → ",
                (bs.keyword_accent, "disable AI features"),
                tag=t.div,
            )
            st_write(bs.cmd, "chat.disableAIFeatures: true", tag=t.div)
        st_space("v", "2.5vh")
        with st_zoom(110), st_block(s.center_txt):
            st_write(bs.body, "Mini guide in the course kit:", tag=t.div)
            st_write(bs.cmd, "ai4se-kit/syllabus/ide-guide.md", link=_GUIDE_URL, tag=t.div)
