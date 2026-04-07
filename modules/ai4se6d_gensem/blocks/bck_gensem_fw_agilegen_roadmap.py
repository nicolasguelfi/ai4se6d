"""Slide — AgileGen: Research Roadmap (short-term vs long-term)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """AgileGen roadmap styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    callout_body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "AgileGen: Research Roadmap", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="24px",
            cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
        ) as g:
            # Left — Short-term
            with g.cell():
                st_write(bs.label, "Short-Term", tag=t.div)
                st_space("v", 0.5)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, "Better ", (bs.keyword, "prompt templates"), " for Gherkin generation")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "AI-aware retrospectives"), " integrating LLM feedback into sprint reviews")

            # Right — Long-term
            with g.cell():
                st_write(bs.stat, "Long-Term", tag=t.div)
                st_space("v", 0.5)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "AI-mediated team coordination"), " \u2014 agents facilitating stand-ups and planning")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Automated sprint planning"), " with workload estimation from historical data")

        st_space("v", 2)
        # Assessment callout
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_body,
                (bs.stat, "Assessment: "),
                "Strong on requirements traceability. "
                "Weak on end-to-end process definition.",
            )
