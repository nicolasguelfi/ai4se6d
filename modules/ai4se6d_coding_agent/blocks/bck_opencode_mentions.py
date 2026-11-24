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

_CODE_ZOOM = 140  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_VAGUE = "Make the home page nicer."
_PRECISE = """\
Read @src/pages/Home.tsx and @tests/App.test.tsx.
Add the subtitle "Track your expenses" to Home,
test first. Do not touch other files."""

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Contrast the vague and the precise prompt; learners try both in Try it 2"
     " (Context)."),
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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Symbol — @ (in opencode)",
     "Type @ in the prompt box, keep typing part of a file name to narrow the list, pick the file: it is attached "
     "to the message. @src/pages/Home.tsx = path from the project folder."),
    ("Prompt — the precise one",
     "« Read @src/pages/Home.tsx and @tests/App.test.tsx » = the files to read. « Add the subtitle … to Home » = "
     "the exact change. « test first » = write the failing test before the code. « Do not touch other files » = "
     "the limit."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "@file — Point, Don’t Hope", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — @file — Point, Don’t Hope", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(120):
            st_write(bs.body, (bs.keyword, "@"), " = fuzzy file search; the file joins the conversation.", tag=t.div)
        st_space("v", "2vh")
        with st_zoom(120), st_grid(cols="5% 90% 5%") as g:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(bs.bad, "Vague — the agent searches and guesses", tag=t.div)
                with st_zoom(_CODE_ZOOM):
                    st_code(s.none, code=_VAGUE, language="text", line_numbers=False, font_size="28pt")
                st_space("v", "3vh")
                st_write(bs.good, "Precise — exactly the context it needs", tag=t.div)
                with st_zoom(_CODE_ZOOM):
                    st_code(s.none, code=_PRECISE, language="text", line_numbers=False, font_size="28pt")
            with g.cell():
                pass  # right margin
