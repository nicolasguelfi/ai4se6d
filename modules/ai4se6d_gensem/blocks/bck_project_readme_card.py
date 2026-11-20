"""Slide — The README project card, written at the 12:00 freeze (exercise E22, edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """README card styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "readme_card_body")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "readme_card_foot")
bs = BlockStyles

_CARD = (
    "# <Project name>\n"
    "<One sentence: who it is for, which problem it solves.>\n"
    "\n"
    "## Run it\n"
    "<the commands to install and start it>\n"
    "\n"
    "## Live\n"
    "<the address — CalcApp's if this project is not deployed>\n"
    "\n"
    "## Known limits\n"
    "- <what does not work yet; each empty shell you kept>\n"
    "\n"
    "## Ethics and compliance\n"
    "<written at 12:15, exercise E23>"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "README: Your Project Card", tag=t.div, toc_lvl="+1", label="README project card")
            st_write(bs.body, "What a visitor reads first — and what the trainer checks at 13:45.", tag=t.div)
            with st_zoom(120):
                st_code(s.none, code=_CARD, language="markdown", line_numbers=False)
            st_write(bs.foot, "Saying your limits yourself is part of the delivery.", tag=t.div)
