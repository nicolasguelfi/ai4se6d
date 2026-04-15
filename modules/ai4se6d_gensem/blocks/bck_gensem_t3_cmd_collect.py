"""Slide — /gse:collect: inventory and classify artefacts from internal and external sources."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t3cc_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t3cc_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t3cc_acc")
bs = BlockStyles


def build():
    st_marker("/gse:collect")
    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, "/gse:collect \u2014 What Do We Have?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:collect \u2014 Artefact Inventory",
                entries=[
                    ("Internal mode", "Scans the current project: source files, tests, docs, config, sprint artefacts, git state, dependencies. Produces .gse/inventory.yaml."),
                    ("External mode", "Provide a path or URL: /gse:collect ~/other-project/ or a GitHub repo. Evaluates reusability, compatibility, integration cost, and license."),
                    ("Reusability assessment", "For each external element: Reusable as-is / Adaptable / Reference only / Incompatible. Integration cost in complexity points."),
                    ("Source registry", "All evaluated sources are recorded in .gse/sources.yaml with SRC- IDs for full provenance traceability."),
                    ("Feeds ASSESS", "The inventory is the input for /gse:assess gap analysis."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            with st_grid(cols="1fr 1fr", gap="24px") as g:
                with g.cell():
                    with st_block(_cell_acc):
                        st_write(bs.keyword + s.center_txt, "Internal Mode")
                        st_space("v", 0.5)
                        st_write(bs.body, "\U0001f4c1 Source files & tests")
                        st_write(bs.body, "\U0001f4cb Sprint artefacts & docs")
                        st_write(bs.body, "\U0001f333 Git state & branches")
                        st_write(bs.body, "\U0001f4e6 Dependencies")
                with g.cell():
                    with st_block(_cell_act):
                        st_write(bs.keyword + s.center_txt, "External Mode")
                        st_space("v", 0.5)
                        st_write(bs.body, "\U0001f4c2 Local projects")
                        st_write(bs.body, "\U0001f310 GitHub repositories")
                        st_write(bs.body, "\U0001f50d Reusability assessment")
                        st_write(bs.body, "\U0001f4dc License check")

            st_space("v", 1)
            st_write(bs.accent, "Output: .gse/inventory.yaml + .gse/sources.yaml (SRC- IDs)")
