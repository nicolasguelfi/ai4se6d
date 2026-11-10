"""Slide — Acceptance criteria in Given / When / Then form (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Acceptance criteria styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "acceptance_body")
    source = s.project.citation + s.large + s.center_txt
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "acceptance_foot")
bs = BlockStyles

_SCENARIO = (
    "Scenario: monthly total of one category\n"
    "  Given expenses of 12.50 and 7.50 in \"Food\" in March\n"
    "    And an expense of 30.00 in \"Transport\" in March\n"
    "  When I open the March summary\n"
    "  Then the \"Food\" total is 20.00\n"
    "    And the \"Transport\" total is 30.00"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, "Acceptance Criteria", tag=t.div, toc_lvl="+1", label="Given / When / Then")
            st_write(bs.body, "Each criterion is an example you could turn into a test.", tag=t.div)
            with st_zoom(130):
                st_code(s.none, code=_SCENARIO, language="gherkin", line_numbers=False)
            st_write(bs.source, cite("north-bdd2006"), tag=t.div)
            st_write(bs.foot, "No criterion, no way to know when the story is done — for you or for the agent.", tag=t.div)
