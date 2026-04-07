"""Slide — The Promptware Crisis: SE lifecycle for prompts."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Promptware crisis styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    callout_title = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_pwc_callout_title",
    )
    callout_body = s.project.titles.body
    message = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_pwc_message",
    )
    source = s.project.titles.source
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Promptware Crisis", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        # Historical parallel callout
        with st_block(s.project.containers.callout):
            st_write(bs.callout_title, "Historical Parallel", tag=t.div)
            st_space("v", 0.5)
            st_write(
                bs.callout_body,
                "Same problems as the ", (bs.stat, "software crisis of the 1970s"),
                ", but for prompts. "
                "Ad hoc management, no versioning, no testing, no governance.",
            )

        st_space("v", 1)

        # Full lifecycle as ordered list
        st_write(bs.body, "The full ", (bs.keyword, "promptware lifecycle"), ":")
        st_space("v", 0.5)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Requirements"), " \u2014 define prompt objectives and constraints")
            with l.item():
                st_write(bs.body, (bs.keyword, "Design"), " \u2014 structure prompt architecture and chains")
            with l.item():
                st_write(bs.body, (bs.keyword, "Implementation"), " \u2014 write and compose prompts")
            with l.item():
                st_write(bs.body, (bs.keyword, "Testing"), " \u2014 evaluate output quality systematically")
            with l.item():
                st_write(bs.body, (bs.keyword, "Debugging"), " \u2014 diagnose and fix prompt failures")
            with l.item():
                st_write(bs.body, (bs.keyword, "Evolution"), " \u2014 version and iterate prompts over time")
            with l.item():
                st_write(bs.body, (bs.keyword, "Deployment"), " \u2014 package and release prompt systems")
            with l.item():
                st_write(bs.body, (bs.keyword, "Monitoring"), " \u2014 track drift and degradation in production")

        st_space("v", 1)
        st_write(
            bs.message,
            "Ad hoc prompt management fails at scale. "
            "Context Engineering is the evolution.",
        )
        st_space("v", 1)
        st_write(bs.source, cite("chen-promptware2025"))
