"""Act IV — VSCodium screenshot alone, maximised: what the agent changed (Source Control diff).

NG, 2026-11-22: a screenshot gets its own slide, as large as the screen allows, with no text —
in a room over 3 m long, a screenshot sharing a slide with text is unreadable.
"""
# Source: ai4se-kit/syllabus/img/ide-2-diff.png (demo CalcApp, no secret, no name)
# @guideline: maximize-viewport
from streamtex import *
from custom.styles import Styles as s


def build():
    st_marker("VSCodium — screenshot")  # its own page, with no visible title
    with st_block(s.project.containers.page_fill_center_wide):
        st_image(uri="images/ide/ide_vscodium_diff.png", width="100%", max_vh=85, align="center")
