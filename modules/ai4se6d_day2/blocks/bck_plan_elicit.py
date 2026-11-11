"""Slide — Eliciting requirements with the plan agent (starter prompt)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Elicitation styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "elicit_body")
    keyword = s.project.titles.keyword
bs = BlockStyles

_PROMPT = """\
I'm building CalcApp v0.1, a personal budget tracker (see @AGENTS.md).
v0.1: add an expense (amount, category, date), list expenses with a
monthly total, two pages with navigation, data kept in localStorage.
My extra ideas: <yours>.
Ask me 3 clarifying questions first. Then propose 4-6 user stories:
title, "As a user, I want...", testable acceptance criteria."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Elicit with the Plan Agent", tag=t.div, toc_lvl="+1")
        st_write(bs.body, (bs.keyword, "Shift+Tab → plan"), ", then adapt and paste:", tag=t.div)
        st_space("v", 0.5)
        st_code(s.none, code=_PROMPT, language="text", line_numbers=False, font_size="22pt")
        st_space("v", 0.5)
        st_write(bs.body, "Read critically. Ask back: errors? fixed or free categories? currency?", tag=t.div)
