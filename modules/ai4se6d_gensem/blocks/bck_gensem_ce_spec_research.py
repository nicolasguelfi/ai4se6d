"""Slide — CE as a Research Platform."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """CE research platform slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "CE as a Research Platform", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                "Transforms CE from a fixed workflow into a ",
                (bs.keyword, "process experimentation platform"),
                ".",
            )

        st_space("v", 0.5)

        st_write(
            bs.body,
            (bs.keyword, "How: "),
            "Researchers define competing process variants, deploy in controlled settings, "
            "collect comparable data, iterate based on evidence.",
        )

        st_space("v", 0.5)

        st_write(
            bs.body,
            "Each iteration only needs modifications to ",
            (bs.keyword, "skill definition files"),
            ", not new tooling.",
        )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "This is how SE methodology evolves: empirically, not dogmatically.",
            )
