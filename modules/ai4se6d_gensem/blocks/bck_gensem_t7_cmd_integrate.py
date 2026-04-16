"""Slide — /gse:integrate: route capitalized solutions to operational destinations."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t7ci_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t7ci_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t7ci_acc")
bs = BlockStyles


def build():
    st_marker("/gse:integrate")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:integrate \u2014 Make It Stick", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:integrate \u2014 Route Solutions",
                entries=[
                    ("Axe 1 \u2192 Project", "Project learnings become config rules or project conventions. Automated patterns are added to .gse/config.yaml."),
                    ("Axe 2 \u2192 GSE-One repo", "Methodology feedback becomes an issue on the GSE-One repository (if the user accepts). Only actionable, validated feedback."),
                    ("Axe 3 \u2192 Learning", "Competency insights are saved to docs/learning/ and the competency map in profile.yaml is updated."),
                    ("Closes the loop", "COMPOUND identifies what was learned. INTEGRATE ensures it is not forgotten \u2014 solutions are routed to operational destinations."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr 1fr", gap="16px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "Axe 1 \u2192 Config")
                        st_space("v", 0.5)
                        st_write(bs.body, "Project rules & conventions")
                        st_write(bs.body, ".gse/config.yaml")
                with g.cell():
                    with st_block(_cell):
                        st_write(bs.keyword + s.center_txt, "Axe 2 \u2192 Issue")
                        st_space("v", 0.5)
                        st_write(bs.body, "GSE-One repo feedback")
                        st_write(bs.body, "User-validated only")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.keyword + s.center_txt, "Axe 3 \u2192 Learning")
                        st_space("v", 0.5)
                        st_write(bs.body, "docs/learning/ notes")
                        st_write(bs.body, "Competency map update")

            st_space("v", 1)
            st_write(bs.accent, "COMPOUND identifies \u2014 INTEGRATE operationalizes. Nothing is forgotten.")
