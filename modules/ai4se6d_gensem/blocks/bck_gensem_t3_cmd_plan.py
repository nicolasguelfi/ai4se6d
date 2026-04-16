"""Slide — /gse:plan: sprint planning at any level, any time."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t3cp_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t3cp_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t3cp_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_LEVELS = [
    ("Project", "Multi-sprint roadmap", "Gate"),
    ("Sprint", "Tasks + complexity budget", "Gate"),
    ("Task", "Implementation approach", "Inform"),
    ("Micro", "Step ordering within activity", "Auto"),
]


def build():
    st_marker("/gse:plan")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:plan \u2014 Plan at Every Level", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:plan \u2014 Cross-Cutting Planning",
                entries=[
                    ("Purpose", "Select items from the backlog pool and promote them to the current sprint. Create new items if needed. Creates the sprint branch at strategic level; assigns branch names to each task at tactical level."),
                    ("4 levels", "Project (roadmap) \u2192 Sprint (budget) \u2192 Task (how) \u2192 Micro (ordering). Each has its own approval tier."),
                    ("Cross-cutting", "Planning is not bound to a single lifecycle phase \u2014 it can be invoked at any abstraction level, at any time (P5)."),
                    ("Re-planning", "Auto-triggered when: task exceeds 2x estimate, new dependency found, assumption invalidated, budget at risk (>80%), or user changes priorities."),
                    ("Planning debt", "If planning is skipped ('just do it'), the agent records planning debt \u2014 reviewed during /gse:compound."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="30% 40% 30%", gap="8px", cell_styles=_hdr_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, "Level")
                with g.cell():
                    st_write(bs.table_hdr, "Scope")
                with g.cell():
                    st_write(bs.table_hdr, "Approval")

            for level, scope, approval in _LEVELS:
                with st_grid(cols="30% 40% 30%", gap="8px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, level)
                    with g.cell():
                        st_write(bs.table_txt, scope)
                    with g.cell():
                        st_write(bs.table_txt, approval)

            st_space("v", 1)
            st_write(bs.accent, "Sprint plan = filtered view of the backlog, not a separate document.")
