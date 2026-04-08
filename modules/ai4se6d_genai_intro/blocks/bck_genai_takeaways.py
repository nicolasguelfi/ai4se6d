"""Slide 13 — Key Takeaways: four summary points + transition phrase."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_top


class BlockStyles:
    """Slide: Takeaways — maximize-viewport archetype: bullet list + transition."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    transition = s.project.titles.body_accent + s.center_txt


bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Key Takeaways", tag=t.div, toc_lvl="1")

            st_space("v", "10vh")
            with st_zoom(130):
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item(): st_write(bs.body, (bs.keyword, "GenAI creates"), " — it generates, not just classifies")
                    with l.item(): st_write(bs.body, (bs.keyword, "LLMs are probabilistic"), " — next-token prediction at scale")
                    with l.item(): st_write(bs.body, (bs.keyword, "Powerful but limited"), " — complement, don't replace expertise")
                    with l.item(): st_write(bs.body, (bs.keyword, "Use responsibly"), " — bias, privacy, transparency matter")

                st_space("h", "2rem")
                st_write(
                    bs.transition,
                    "Next: VibeCoding — from intent to code",
                    tag=t.div,
                )
