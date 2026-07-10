"""Slide — Specialization: two paths to make GSE-One your own."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """GSE-One specialization slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    path_title = s.bold + s.project.colors.highlight
    locator = s.project.colors.muted
    teaser = s.project.titles.body + s.project.colors.highlight + s.bold
bs = BlockStyles

def build():
    st_marker("Making GSE-One Your Own")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Specialization — Making GSE-One Your Own", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="GSE-One Specialization",
                        entries=[
                            ("Two paths", "Light, per-project specialization = configure via .gse/config.yaml (no fork). Deep specialization = derive your own methodology by forking the repo."),
                            ("The doctrine", "The methodology itself stays generic — specialization lives in each project's config, or in your own derived methodology repo. Never wire a technology or a case study into the method."),
                            ("Fork tooling included", "The repo ships a generator (gse_generate.py --verify), a cross-platform installer (install.py), and a meta-audit tool for forkers."),
                            ("License", "GSE-One is under the Business Source License 1.1 — check its terms before distributing a derivative."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

        with st_zoom(100):
            st_write(bs.body, "Two paths to make GSE-One your own:")
            st_space("v", 1)

            st_write(bs.body, (bs.path_title, "Path 1 — Configure"), " (per project, no fork) — everything in ", (bs.keyword, ".gse/config.yaml"), " (spec §13):")
            with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Phases on/off & order"), " — toggle LC02 activities, or set a custom ", (bs.locator, "order"), " list")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Decision calibration"), " — ", (bs.locator, "tier_bias"), " (hands-off / balanced / hands-on) + ", (bs.locator, "always_gate"), " list")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Guardrail sensitivity"), " — ", (bs.locator, "relaxed / standard / strict"), " (or auto, from your profile)")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Budget & health"), " — ", (bs.locator, "complexity.budget_per_sprint"), ", ", (bs.locator, "health.disabled_dimensions"))
                with l.item():
                    st_write(bs.body, (bs.keyword, "Domain & team"), " — ", (bs.locator, "project.domain"), " (9 values), per-user profiles in ", (bs.locator, ".gse/profiles/"))

            st_space("v", 1)

            st_write(bs.body, (bs.path_title, "Path 2 — Derive your own methodology"), " (fork the methodology repo):")
            with st_list(li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Define your process model"), " — edit ", (bs.locator, "gse-one/src/"), " (activities, principles, templates — the single source of truth)")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Create your variant activity/skill files"), " — ", (bs.locator, "src/activities/*.md"), " are the skill sources")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Regenerate & verify"), " — ", (bs.locator, "python3 gse_generate.py --verify"), " rebuilds the plugin for all 5 platforms, with parity checks")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Install & audit your fork"), " — ", (bs.locator, "install.py"), " from your fork; the meta-audit tool ships for forkers")
            st_write(bs.body, (bs.locator, "License note: Business Source License 1.1 — check its terms before distributing a derivative."))

            st_space("v", 1)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.teaser,
                    "GenSEMOne (Part 5) is this course's own example of Path 2 — "
                    "a lightweight derived method using only Cursor native features.",
                )
