"""Slide — The 160,000-Developer Study (Daniotti et al.)."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero_primary
    body = s.project.titles.body
    label = s.project.titles.label
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "The 160,000-Developer Study",
                tag=t.div, toc_lvl="1",
            )
            st_space("v", 1)
            st_write(bs.stat, "160K+")
            st_space("v", 1)
            st_write(
                bs.body,
                "Daniotti et al. analyzed GitHub developers. "
                "Contradicts conventional wisdom:",
            )

        st_space("v", 2)
        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "Experienced senior-level programmers capture nearly ",
                (bs.label, "ALL"), " measurable productivity gains. "
                "Early-career programmers show ",
                (s.bold + s.project.colors.critical, "NO"),
                " significant benefits.",
            )

        st_space("v", 1)
        st_write(
            bs.body,
            "Controlled enterprise settings (juniors get structured support) "
            "vs. open-source (AI tools reward existing expertise).",
        )

        st_space("v", 1)
        st_write(bs.source, cite("daniotti-github2025"))
