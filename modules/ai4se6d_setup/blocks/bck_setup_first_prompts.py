"""Slide — Suggested first prompts for the three ideas."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """First prompts slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    label = s.project.titles.label
bs = BlockStyles

_CODE_ZOOM = 150  # st_code font_size is not applied by Pygments: zoom instead
_PROMPTS = [
    ("Recipe Finder", "Create a Recipe Finder web app: type ingredients, see recipes."),
    ("Habit Tracker", "Build a Habit Tracker web app: daily check-off and streaks."),
    ("Movie Watchlist", "Create a Movie Watchlist web app: save movies, rate them 1-5."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "First Prompts", tag=t.div, toc_lvl="1")
        for name, prompt in _PROMPTS:
            with st_block(s.none):
                st_write(bs.label, name, tag=t.div)
                with st_zoom(_CODE_ZOOM):
                    st_code(s.none, code=prompt, language="text", line_numbers=False)
