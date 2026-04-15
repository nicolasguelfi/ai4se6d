"""Slide — /gse:status: show lifecycle status at a glance."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t2cs_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t2cs_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t2cs_acc")
bs = BlockStyles


def build():
    st_marker("/gse:status")
    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, "/gse:status \u2014 Where Am I?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:status \u2014 Lifecycle Status",
                entries=[
                    ("Purpose", "Display the current state of your project at a glance: sprint, phase, artifacts, health, branches."),
                    ("When to use", "Anytime you need orientation \u2014 beginning of session, after a pause, or before deciding what to do next."),
                    ("What it shows", "Current sprint number, active lifecycle phase (LC00\u2013LC03), artifact inventory, pending reviews, health score, active branches and worktrees."),
                    ("Cross-cutting", "Available at any phase \u2014 does not change project state, purely informational."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            st_write(bs.accent, "Your project dashboard \u2014 always available, never modifies state.")
            st_space("v", 1)

        with st_zoom(90):
            _status_left = [
                ("\U0001f3c3", "Current Sprint"),
                ("\U0001f4cd", "Active Phase"),
                ("\U0001f4e6", "Artifact Inventory"),
            ]
            _status_right = [
                ("\U0001f50d", "Pending Reviews"),
                ("\U0001f4ca", "Health Score"),
                ("\U0001f333", "Branches & Worktrees"),
            ]
            with st_grid(cols="1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                        for icon, label in _status_left:
                            with inner.cell():
                                st_write(bs.body, f"{icon} ", (bs.keyword, label))
                with g.cell():
                    with st_grid(cols="1fr", gap="12px", cell_styles=_cell) as inner:
                        for icon, label in _status_right:
                            with inner.cell():
                                st_write(bs.body, f"{icon} ", (bs.keyword, label))
