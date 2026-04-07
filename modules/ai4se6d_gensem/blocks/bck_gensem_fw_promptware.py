"""Slide — Promptware Engineering: SE lifecycle applied to prompts."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Promptware Engineering slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    callout_title = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_pw_callout_title",
    )
    callout_body = s.project.titles.body
    assessment = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_pw_assessment",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Promptware Engineering", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="24px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            # Left — callout with lifecycle steps
            with g.cell():
                with st_block(s.project.containers.callout):
                    st_write(bs.callout_title, "Prompt Lifecycle", tag=t.div)
                    st_space("v", 1)
                    with st_list(l_style=bs.callout_body, li_style=bs.callout_body, list_type=lt.ordered) as l:
                        with l.item():
                            st_write(bs.callout_body, "Requirements \u2192 Define prompt objectives")
                        with l.item():
                            st_write(bs.callout_body, "Design \u2192 Structure prompt architecture")
                        with l.item():
                            st_write(bs.callout_body, "Implementation \u2192 Write and chain prompts")
                        with l.item():
                            st_write(bs.callout_body, "Testing \u2192 Evaluate output quality")
                        with l.item():
                            st_write(bs.callout_body, "Maintenance \u2192 Version and evolve prompts")

            # Right — key points
            with g.cell():
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Authors: "), "Chen et al. \u2014 SE lifecycle mapped to prompt systems")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Promptware crisis: "), "Unmanaged prompts degrade like unmaintained code")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Context Engineering: "), "Evolution toward managing full context windows, not just prompts")
                    with l.item():
                        st_write(bs.body, (bs.keyword, "Implication: "), "Prompts are first-class software artifacts requiring versioning and testing")

        st_space("v", 2)
        st_write(bs.assessment, "Valuable lens \u2014 connects naturally to Context Engineering practices.")
        st_write(bs.source, "Chen et al. \u2014 Promptware Engineering, 2023")
