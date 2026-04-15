"""Slide — /gse:assess: evaluate artefact status and identify gaps."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t3ca_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t3ca_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t3ca_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t3ca_hl")
bs = BlockStyles


def build():
    st_marker("/gse:assess")
    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, "/gse:assess \u2014 What Is Missing?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:assess \u2014 Gap Analysis",
                entries=[
                    ("Input", "Artefact inventory from /gse:collect + project goals from config or user."),
                    ("Analysis", "For each goal: which artefacts exist? Which are missing? What is their status (draft/reviewed/approved)? For external sources: compatibility and integration cost."),
                    ("Output", "Gap analysis report with GAP-NN identifiers: \u2713 Covered, \u25d0 Partial, \u2717 Uncovered, \u26a0 Risk areas."),
                    ("Feeds PLAN", "Uncovered goals (GAP-NN) become candidate TASK items in the backlog pool."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr 1fr", gap="12px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "\u2713 Covered")
                        st_space("v", 0.5)
                        st_write(bs.body, "Artefacts exist and are complete")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "\u25d0 Partial")
                        st_space("v", 0.5)
                        st_write(bs.body, "Exist but incomplete or unreviewed")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.highlight, "\u2717 Uncovered")
                        st_space("v", 0.5)
                        st_write(bs.body, "No artefacts \u2192 GAP-NN created")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.highlight, "\u26a0 Risk")
                        st_space("v", 0.5)
                        st_write(bs.body, "High-complexity or security-sensitive")

            st_space("v", 1)
            st_write(bs.accent, "GAP-NN items feed directly into /gse:plan as candidate tasks.")
