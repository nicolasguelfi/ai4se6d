"""Slide — The Homogenization Effect on creativity."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Creativity/homogenization styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    source = s.project.citation + s.large + s.center_txt

bs = BlockStyles


def build():
    st_marker("Homogenization Risk")
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Homogenization Effect", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="Homogenization and Creativity Risk",
            entries=[
                ("Risk", "AI-assisted solutions converge toward similar patterns, reducing diversity."),
                ("Evidence", "TOSEM identifies 5 interconnected themes on creativity impact."),
                ("Social impact", "Xiao study: engineers consult AI instead of colleagues, disrupting knowledge sharing."),
                ("GSE-One link", "GSE-One /gse:review phase explicitly checks for creative diversity and avoids monoculture."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 1)

        with st_zoom(120):
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        "AI-assisted solutions ",
                        (bs.stat, "converge toward similar patterns"),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "TOSEM: ",
                        (bs.keyword, "5 interconnected themes"),
                        " on creativity impact",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "A concern ",
                        (bs.stat, "beyond productivity metrics"),
                    )

            st_space("v", 1)
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    "Xiao longitudinal study: engineers consult AI ",
                    (bs.keyword, "instead of colleagues"),
                    ". Knowledge-sharing dynamics disrupted.",
                )

            st_space("v", 1)
            st_write(bs.source, cite("xiao-longitudinal2025"))
