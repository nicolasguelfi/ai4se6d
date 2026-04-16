"""Slide — SE 3.0: Adaptive Partnership + Multi-Objective + SLA-Aware."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """SE 3.0 adaptive slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    callout_body = s.project.titles.body
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "SE 3.0: Adaptive Partnership + Multi-Objective", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Adaptive AI partnership: "),
                    "Copilots evolving to collaborators to ",
                    (bs.stat, "autonomous agents"),
                    ". The AI adapts its level of initiative to the developer\u2019s skill and context.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "Multi-objective code synthesis: "),
                    "Balancing quality, performance, and security ",
                    (bs.label, "simultaneously"),
                    " \u2014 not as afterthoughts but as primary generation constraints.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.keyword, "SLA-aware execution: "),
                    "AI is aware of non-functional constraints (latency, throughput, cost) "
                    "and generates code that respects them by design.",
                )

        st_space("v", 2)
        # Assessment callout
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_body,
                (bs.stat, "Assessment: "),
                "Most ambitious vision. Largely theoretical \u2014 ",
                (bs.keyword, "no reference implementation yet"),
                ".",
            )
