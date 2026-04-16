"""Slide — Agentic DevOps: Microsoft's vision for AI agents in CI/CD."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Agentic DevOps slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    stat = s.bold + s.project.colors.highlight
    callout_title = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_adev_callout_title",
    )
    callout_body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

def build():
    st_marker("Agentic DevOps (Microsoft)")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Agentic DevOps", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Agentic DevOps — Microsoft Vision",
                        entries=[
                            ("Key idea", "Extends DevOps with autonomous AI agents for CI/CD, provisioning, and incident response."),
                            ("Vision vs product", "Agentic DevOps is a strategic vision, not a deployed product. However, concrete elements already exist: GitHub Copilot Agent Mode (autonomous multi-file edits), coding agent in Actions (async CI/CD agents), and Agent HQ (agent monitoring dashboard)."),
                            ("Limitations", "Requires platform engineering maturity (85% of practitioners agree). Few production-grade implementations of the full vision. 7h/week lost to AI-generated debt (GitLab 2025)."),
                            ("GSE-One gap", "GSE-One provides process discipline and knowledge capitalization that Agentic DevOps does not address."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )

        with st_zoom(90):
            with st_grid(
                cols=s.project.containers.responsive_2col,
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                # Left — callout with key stat
                with g.cell():
                    with st_block(s.project.containers.callout):
                        st_write(bs.callout_title, "The AI Paradox", tag=t.div)
                        st_space("v", 1)
                        st_write(bs.callout_body, "Developers report saving time with AI coding assistants, yet ", (bs.stat, "7h/week"), " are lost to AI-generated technical debt.")
                        st_space("v", 1)
                        st_write(bs.callout_body, (bs.stat, "85%"), " of organizations need platform engineering to manage the complexity AI introduces.")

                # Right — bullet list
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Vision: "), "Microsoft\u2019s extension of DevOps with autonomous AI agents")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Scope: "), "Agents manage CI/CD pipelines, infrastructure provisioning, incident response")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Prerequisite: "), "Platform engineering maturity to control agent boundaries")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Status: "), "Emerging \u2014 few production-grade implementations")

            st_space("v", 1)
            st_write(bs.source, cite("microsoft-agenticdevops2025"))
