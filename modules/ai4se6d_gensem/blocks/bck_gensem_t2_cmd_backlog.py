"""Slide — /gse:backlog: unified work item management."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell
_active_cell = s.project.containers.table_active_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2cb_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2cb_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2cb_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_SUBCMDS = [
    ("/gse:backlog", "Show full backlog (pool + sprint)"),
    ("/gse:backlog add <desc>", "Add a new item to the pool"),
    ("/gse:backlog sprint", "Show current sprint items only"),
    ("/gse:backlog pool", "Show unplanned items only"),
    ("/gse:backlog --type code", "Filter by artifact type"),
    ("/gse:backlog sync", "Synchronize with GitHub Issues"),
]


def build():
    st_marker("/gse:backlog")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:backlog \u2014 Unified Work Items", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:backlog \u2014 Pool + Sprint",
                entries=[
                    ("Two zones", "Pool = unplanned ideas (sprint: null). Sprint = items assigned to current sprint. Items move from pool to sprint during /gse:plan."),
                    ("Auto-populated", "The agent adds items automatically: /gse:review findings, /gse:collect imports, /gse:plan deferrals. You can also add manually."),
                    ("Artifact types", "Filter by: code, test, requirement, design, doc, config, import, spike."),
                    ("GitHub sync", "/gse:backlog sync two-way synchronizes with GitHub Issues. Gate confirmation if conflicts detected."),
                    ("Cross-cutting", "Available at any phase. The backlog is the single source of truth for all work items."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            # Sub-commands table
            with st_grid(cols="45% 55%", gap="8px", cell_styles=_hdr_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, "Command")
                with g.cell():
                    st_write(bs.table_hdr, "Description")

            for cmd, desc in _SUBCMDS:
                with st_grid(cols="45% 55%", gap="8px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, cmd)
                    with g.cell():
                        st_write(bs.table_txt, desc)

            st_space("v", 1)
            st_write(bs.accent, "Single source of truth \u2014 auto-populated by review, collect, and plan.")
