"""Slide — online survey on Sumvadis, right after the participants' round table (NG, 2026-11-22).

QR code + clickable URL + illustration + the Sumvadis wordmark, readable from the back of the room.
"""
# Assets (static/images/survey/):
#   survey_qr.png                 — QR of _SURVEY_URL (qrcode, error correction M; decoded back to the URL)
#   survey_sumvadis_wordmark.png  — Sumvadis wordmark, copied from sumvadis/apps/events/brand/ (gradient, reads on dark)
#   survey_illustration.webp      — gpt-image-2, prompt in survey_illustration.prompt.txt
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_SURVEY_URL = "https://app.sumvadis.ai/s/55441001"
_SURVEY_SHOWN = "app.sumvadis.ai/s/55441001"   # what is read aloud and typed; the link stays the full URL
_IMG = "images/survey"


class BlockStyles:
    """Survey slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    caption = Style.create(s.project.titles.caption + s.center_txt, "poll_survey_caption")
    url = Style.create(
        s.Large + s.text.fonts.font_monospace + s.bold + s.project.colors.accent + s.center_txt,
        "poll_survey_url",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_image(uri=f"{_IMG}/survey_sumvadis_wordmark.png", width="22vw", align="center", link=_SURVEY_URL)
            st_write(bs.heading, "Quick Survey", tag=t.div, toc_lvl="1")
            st_write(bs.caption, "Scan the QR code with your phone, or open the link", tag=t.div)

            with st_grid(cols="1.5fr 3.5fr", gap="48px", cell_styles=s.project.containers.grid_cell_centered) as g:
                with g.cell():
                    st_image(uri=f"{_IMG}/survey_illustration.webp", width="100%", max_vh=58, align="center")
                with g.cell():
                    st_image(uri=f"{_IMG}/survey_qr.png", width="100%", max_vh=50, align="center",
                             link=_SURVEY_URL)
                    st_write(bs.url, _SURVEY_SHOWN, link=_SURVEY_URL, tag=t.div)
