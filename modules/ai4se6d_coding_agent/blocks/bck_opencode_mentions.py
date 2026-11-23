"""Slide — @file mentions: point, don't hope."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Mentions styles."""
    heading = s.project.titles.heading
    bad = Style.create(s.project.titles.subtitle + s.project.colors.critical, "ocstr_bad")
    good = Style.create(s.project.titles.subtitle + s.project.colors.success, "ocstr_good")
    body = Style.create(s.project.titles.body + s.center_txt, "ment_body")
    keyword = s.project.titles.keyword
bs = BlockStyles

_VAGUE = "Make the home page nicer."
_PRECISE = """\
Read @src/pages/Home.tsx and @tests/App.test.tsx.
Add the subtitle "Track your expenses" to Home,
test first. Do not touch other files."""

_NOTES = [
    ("The message",
     "Typing @ opens a fuzzy file search; the chosen file joins the conversation. You decide what the agent reads "
     "instead of hoping it finds it."),
    ("Vague",
     "« Make the home page nicer »: the agent searches, guesses which files matter and what « nicer » means."),
    ("Precise",
     "The precise prompt names the two files to read, the exact change, the order (test first) and the limit "
     "(do not touch other files)."),
    ("The trap",
     "Mentioning the whole project « just in case ». Every file takes room in the context window: point at what "
     "the task needs."),
    ("Ask the room",
     "« Rewrite your last vague prompt: which files would you @mention? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "@file — Point, Don’t Hope", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — @file — Point, Don’t Hope", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(125):
            st_write(bs.body, (bs.keyword, "@"), " = fuzzy file search; the file joins the conversation.", tag=t.div)
        st_space("v", "2vh")
        with st_zoom(125), st_grid(cols="5% 90% 5%") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(bs.bad, "Vague — the agent searches and guesses", tag=t.div)
                st_code(s.none, code=_VAGUE, language="text", line_numbers=False, font_size="28pt")
                st_space("v", "3vh")
                st_write(bs.good, "Precise — exactly the context it needs", tag=t.div)
                st_code(s.none, code=_PRECISE, language="text", line_numbers=False, font_size="28pt")
            with g.cell():
                pass  # right margin
