"""Slide — Reality check: Anthropic finding, Bain study, gala dinner pivot."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s

class BlockStyles:
    """Reality check slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    stat_big = Style.create(
        s.GIANT + s.bold + s.project.colors.primary + s.center_txt,
        "vc_reality_stat_big",
    )
    stat_warn = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_reality_stat_warn",
    )
    body = s.project.titles.body + s.center_txt
    source = s.project.titles.caption + s.center_txt
    keyword_ok = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.bold + s.italic + s.project.colors.highlight + s.center_txt,
        "vc_reality_emphasis",
    )
bs = BlockStyles

def build():
    # Slide 27 — Anthropic Finding
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.heading, "What Can Actually Be Delegated?", tag=t.div, toc_lvl="1")
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.stat_big, "60% "),
                "integrable",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.stat_warn, "0\u201320% "),
                "fully delegable",
            )
            st_space("v", 2)
            st_write(
                bs.body,
                "Most work still needs human judgment, review, and direction.",
            )
            # REF: https://www.anthropic.com/research/impact-software-development
            st_write(bs.source, cite("anthropic2025impact"))

    st_slide_break()

    # Slide 28 — Bain Study
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(bs.heading, "Process > Tools", tag=t.div, toc_lvl="2")
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.stat_warn, "10% "),
                "gains without process change",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.stat_big, "25\u201330% "),
                "with end-to-end process redesign",
            )
            st_space("v", 2)
            st_write(
                bs.body,
                "Tools alone are not enough.",
            )
            # REF: https://www.bain.com/insights/topics/technology-report/
            st_write(bs.source, cite("bain2025techreport"))

    st_slide_break()

    # Slide 29 — Naive VibeCoding Has Its Place (gala dinner pivot)
    with st_block(s.project.containers.page_fill_center_noalign):
        with st_block(s.center_txt):
            st_write(bs.heading, "It Has Its Place", tag=t.div, toc_lvl="2")
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword_ok, "At home: "),
                "personal prototypes, throwaway demos, learning, exploring ideas.",
            )
            st_space("v", 1)
            st_write(
                bs.body,
                (bs.keyword_warn, "Not for: "),
                "production, enterprise, regulated environments, shared code.",
            )
            st_space("v", 2)
            st_write(
                bs.emphasis,
                "Now imagine your restaurant hosts a gala dinner for 200 guests. "
                "Individual dietary requirements. Press in attendance. "
                "Would you cook the same way?",
            )
