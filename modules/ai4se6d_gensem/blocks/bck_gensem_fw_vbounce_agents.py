"""Slide — V-Bounce: Multi-Agent Role Assignments."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """V-Bounce agent roles styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    callout_body = s.project.titles.body
    stat = s.project.titles.stat
    source = s.project.titles.source
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "V-Bounce: Multi-Agent Role Assignments", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(300px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
        ) as g:
            with g.cell():
                st_write(bs.label, "Project Scope Agent", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, "Manages ", (bs.keyword, "requirements and boundaries"), ". Ensures the project stays within defined scope.")

            with g.cell():
                st_write(bs.label, "QA Agent", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, "Defines and monitors ", (bs.keyword, "quality criteria"), ". Acts as an automated quality gate at each V-level.")

            with g.cell():
                st_write(bs.label, "Planning Agent", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, (bs.keyword, "Decomposes work"), " and schedules tasks. Coordinates the bounce sequence between phases.")

            with g.cell():
                st_write(bs.label, "Implementation Agent", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, "Generates ", (bs.keyword, "code within constraints"), " set by the other agents. Iterates until validation passes.")

        st_space("v", 2)
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_body,
                "One of the first ", (bs.stat, "formally defined AI-native SDLCs"),
                " with explicit agent role assignments.",
            )

        st_space("v", 1)
        st_write(bs.source, cite("hymel-vbounce2025"))
