"""Slide — CE Design Philosophy: 80/20 rule and artifact-driven composition."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """CE philosophy slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    card_title = s.bold + s.project.colors.primary + s.Large
    callout_text = s.project.titles.body + s.project.colors.highlight
    antipattern = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

def build():
    st_marker("GSE-One: Design Philosophy")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Design Philosophy", tag=t.div, toc_lvl="1")
                with g.cell():
                    st_hover_tooltip(
                        title="GSE-One Design Philosophy",
                        entries=[
                            ("Core idea", "Each unit of engineering work should make subsequent units easier, not harder."),
                            ("80/20 rule", "~80% planning and review, ~20% execution -- inverts VibeCoding."),
                            ("GSE-One equivalent", "This philosophy underpins all /gse: commands, especially /gse:assess and /gse:plan."),
                            ("Anti-pattern", "The 'prompt, generate, pray' loop with no planning or review."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(75):
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.antipattern, "Anti-pattern: "),
                    "the \"prompt, generate, pray\" loop \u2014 no planning, no review, "
                    "no knowledge retention.",
                )


            st_space("v", 1)

            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="24px",
                cell_styles=s.project.containers.cell_pad_md,
            ) as g:
                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.card_title, "The 80/20 Rule", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, (bs.keyword, "~80%"), " planning and review")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "~20%"), " execution")
                            with l.item():
                                st_write(bs.body, "Inverts the typical AI-assisted distribution")
                            with l.item():
                                st_write(bs.body, "Quality comes from preparation, not generation speed")

                with g.cell():
                    with st_block(s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md):
                        st_write(bs.card_title, "Artifact-Driven Composition", tag=t.div)
                        st_space("v", 0.5)
                        with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Artefact-centric lifecycle"), " \u2014 every activity produces a traceable deliverable")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Adaptive ordering"), " \u2014 the orchestrator (/gse:go) detects state and proposes the next step")
                            with l.item():
                                st_write(bs.body, (bs.keyword, "Guardrail-bounded flexibility"), " \u2014 phases follow constraints, not a rigid sequence")

            st_space("v", 1)

