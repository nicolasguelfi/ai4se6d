"""Slide — Hands-up quiz on day 1: five true/false statements (answers on the next slide)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Quiz slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
bs = BlockStyles

# Keep in the same order as _ANSWERS in bck_setup_quiz_answers.py (next slide).
_STATEMENTS = [
    "The model remembers yesterday's chat.",
    "Every token sent and received costs money.",
    "Pasting your API key in a prompt is fine.",
    "Vibe coding = accepting AI code unread.",
    "A commit is a save point you can return to.",
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Hands-Up Quiz", tag=t.div, toc_lvl="1")
        st_write(bs.body, "True or false? ", (bs.keyword, "Hands up for TRUE."))
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            for statement in _STATEMENTS:
                with l.item():
                    st_write(bs.body, statement)
