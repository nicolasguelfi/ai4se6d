"""Act IV — VSCodium: the recommended editor, install and switch its AI off (NG, 2026-11-22).

Text only: the screenshot has its own slide right after (bck_ide_vscodium_capture) — NG, 2026-11-22:
a screenshot and text on the same slide are unreadable in a room over 3 m long.
"""
# Source: ai4se-kit/syllabus/ide-guide.md (kit 2026-11-22.3); chat.disableAIFeatures checked in VSCodium 1.112.
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


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

_CODE_ZOOM = 150  # st_code font_size is not applied by Pygments: zoom instead
_INSTALL = (
    "brew install --cask vscodium                  # macOS\n"
    "winget install VSCodium.VSCodium              # Windows\n"
    "flatpak install flathub com.vscodium.codium   # Linux"
)
_GUIDE_URL = "https://github.com/nicolasguelfi/ai4se-kit/blob/main/syllabus/ide-guide.md"


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "VSCodium", tag=t.div, toc_lvl="1")
        st_write(
            bs.caption,
            "The open-source build of VS Code: free, no Copilot account, no Microsoft telemetry.",
            tag=t.div,
        )
        with st_zoom(_CODE_ZOOM):
            st_code(s.none, code=_INSTALL, language="bash", line_numbers=False)
        with st_block(bs.box):
            st_write(
                bs.body, (bs.keyword_warn, "Once: "), "Settings → ",
                (bs.keyword_accent, "disable AI features"),
                tag=t.div,
            )
            st_write(bs.cmd, "chat.disableAIFeatures: true", tag=t.div)
        with st_block(s.center_txt):
            st_write(bs.body, "Mini guide in the course kit:", tag=t.div)
            st_write(bs.cmd, "ai4se-kit/syllabus/ide-guide.md", link=_GUIDE_URL, tag=t.div)
