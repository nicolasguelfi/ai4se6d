"""Slide — The Copilot Effect: what the largest RCT tells us."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Copilot RCT stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = Style.create(
        s.GIANT + s.bold + s.project.colors.primary + s.center_txt,
        "ve_evidence_rct_stat",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large + s.center_txt
    transition = Style.create(
        s.Large + s.italic + s.center_txt + s.project.colors.muted,
        "ve_evidence_rct_transition",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Copilot Effect", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.stat, "+55.8%")
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "Faster task completion with GitHub Copilot.",
                    )
                    st_space("v", 0.5)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "95"), " professional programmers")
                        with l.item():
                            st_write(bs.body, "Task: HTTP server in JavaScript")
                        with l.item():
                            st_write(bs.body, "95% CI: 21%\u201389%, p=0.0017")
                    st_space("v", 0.5)
                    # REF: Peng et al. 2023, arXiv 2302.06590
                    st_write(bs.source, cite("peng-copilot2023"))

                with g.cell():
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "But:"),
                        " single task, controlled environment.",
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "METR study (real projects): ",
                        (bs.keyword_warn, "\u221219%"),
                        " slower.",
                    )
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        "The difference?",
                    )
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Complexity"), " \u2014 toy task vs. mature codebase")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Familiarity"), " \u2014 new project vs. 5+ years experience")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Discipline"), " \u2014 structured process vs. ad hoc")
                    st_space("v", 0.5)
                    st_write(
                        bs.body,
                        (bs.keyword, "Simple tasks = AI shines."),
                    )
                    st_write(
                        bs.body,
                        (bs.keyword_warn, "Complex real-world = discipline required."),
                    )

            st_space("v", 1)
            st_write(bs.transition, "Who benefits the most? \u2192")
