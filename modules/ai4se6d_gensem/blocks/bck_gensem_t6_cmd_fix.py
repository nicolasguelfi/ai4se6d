"""Slide — /gse:fix: apply fixes with traceability to review findings."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t6cf_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t6cf_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t6cf_acc")
bs = BlockStyles


def build():
    st_marker("/gse:fix")
    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, "/gse:fix \u2014 Fix What Was Found", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:fix \u2014 Traceable Corrections",
                entries=[
                    ("Input", "RVW- findings from /gse:review with severity levels."),
                    ("Isolation", "Creates a fix branch from the reviewed branch. Fixes are applied in an isolated worktree."),
                    ("Traceability", "Each fix traces back to its RVW- finding. The review/fix cycle is iterable until all findings are resolved."),
                    ("Iterative", "/gse:review \u2192 /gse:fix \u2192 /gse:review \u2192 ... until quality is satisfactory."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr", gap="24px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "\U0001f50d /gse:review")
                        st_space("v", 0.5)
                        st_write(bs.body, "Identifies RVW- findings")
                        st_write(bs.body, "Assigns severity levels")
                        st_write(bs.body, "Updates health score")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "\U0001f527 /gse:fix")
                        st_space("v", 0.5)
                        st_write(bs.body, "Creates fix branch")
                        st_write(bs.body, "Applies fixes in worktree")
                        st_write(bs.body, "Traces to RVW- IDs")

            st_space("v", 1)
            st_write(bs.accent, "Review \u2192 Fix \u2192 Review \u2014 iterate until quality is right.")
