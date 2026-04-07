"""Slide — The AI Paradox: 7h/week lost to AI inefficiencies."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "gs_ev_paradox_ai_stat",
    )
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The AI Paradox", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            st_write(bs.stat, "7h")
            st_space("v", 1)
            st_write(
                bs.body,
                "Lost per team member weekly to AI-related inefficiencies (GitLab 2025). "
                "Faster coding creates bottlenecks elsewhere: review, debugging, integration.",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword, "85%"),
                " recognize platform engineering as essential to manage the complexity.",
            )

        st_space("v", 1)
        st_write(bs.source, cite("gitlab-devsecops2025"))
