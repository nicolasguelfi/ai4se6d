"""Slide — @file mentions: point, don't hope."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Mentions styles."""
    heading = s.project.titles.heading
    bad = Style.create(s.project.titles.subtitle + s.project.colors.critical, "d2_ocstr_bad")
    good = Style.create(s.project.titles.subtitle + s.project.colors.success, "d2_ocstr_good")
    body = Style.create(s.project.titles.body + s.center_txt, "d2_ment_body")
    keyword = s.project.titles.keyword
bs = BlockStyles

_VAGUE = "Make the home page nicer."
_PRECISE = """\
Read @src/pages/Home.tsx and @tests/App.test.tsx.
Add the subtitle "Track your expenses" to Home,
test first. Do not touch other files."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "@file — Point, Don’t Hope", tag=t.div, toc_lvl="+1")
        st_write(bs.body, (bs.keyword, "@"), " = fuzzy file search; the file joins the conversation.", tag=t.div)
        st_space("v", 0.5)
        st_write(bs.bad, "Vague — the agent searches and guesses", tag=t.div)
        st_code(s.none, code=_VAGUE, language="text", line_numbers=False, font_size="24pt")
        st_write(bs.good, "Precise — exactly the context it needs", tag=t.div)
        st_code(s.none, code=_PRECISE, language="text", line_numbers=False, font_size="24pt")
