"""Slide — AgileGen: Memory Pool + Practitioner Frustrations."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """AgileGen memory pool styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    callout_title = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_agm_callout_title",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "AgileGen: Memory Pool + Frustrations", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="24px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            # Left — Memory pool mechanism
            with g.cell():
                with st_block(s.project.containers.callout):
                    st_write(bs.callout_title, "Memory Pool Mechanism", tag=t.div)
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "Collects decision-making scenarios from past sprints. "
                        "When new users face similar requirements, the pool ",
                        (bs.keyword, "recommends proven patterns"),
                        " \u2014 accelerating onboarding and reducing rework.",
                    )

            # Right — XP2025 frustrations
            with g.cell():
                st_write(bs.label, "XP2025 Workshop Frustrations", tag=t.div)
                st_space("v", 0.5)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Tooling fragmentation: "), "too many disconnected AI tools in the pipeline")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Governance gaps: "), "no clear policies for AI-generated artifacts")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Data quality issues: "), "LLM outputs inconsistent across sprints")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Skill deficits: "), "teams lack prompt engineering and AI literacy")

        st_space("v", 1)
        st_write(bs.source, cite("zhang-agilegen2025"))
