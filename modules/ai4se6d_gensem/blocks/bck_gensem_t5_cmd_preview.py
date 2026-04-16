"""Slide — /gse:preview: see before building."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t5cp_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t5cp_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t5cp_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_PREVIEW_TYPES = [
    ("UI feature", "Wireframe description, screen-by-screen walkthrough"),
    ("API", "Example request/response pairs, endpoint summary"),
    ("Architecture", "Component diagram (mermaid), dependency map"),
    ("Data model", "Entity list, relationship description"),
    ("Feature", "User story walkthrough: \u201cAs a user, I click X, I see Y\u201d"),
    ("Imported element", "Side-by-side: original source vs. planned adaptation"),
]


def build():
    st_marker("/gse:preview")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:preview \u2014 See Before Building", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:preview \u2014 Close the Gap",
                entries=[
                    ("Purpose", "Simulate what planned artifacts will look like BEFORE any code is written. Lightweight \u2014 not a prototype, but a visualization."),
                    ("Why it matters", "Closes the gap between 'I described what I want' and 'I can see what I'll get.' Fixing design costs 10x less than fixing code."),
                    ("Gate decision", "The user validates the preview before production starts. Modifications can be requested before any code is generated."),
                    ("When used", "After /gse:reqs and /gse:design, before /gse:tests and /gse:produce. The preview informs both test strategy and implementation."),
                    ("In CalcApp", "Preview the budget dashboard wireframe, the StorageService API contract, and the expense form user journey."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            st_write(bs.accent, "Plan 80%, execute 20% \u2014 preview closes the 80%.")
            st_space("v", 1)

            # Preview types table
            with st_grid(cols="25% 75%", gap="8px", cell_styles=_hdr_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, "Artifact Type")
                with g.cell():
                    st_write(bs.table_hdr, "Preview Format")

            for art_type, preview_format in _PREVIEW_TYPES:
                with st_grid(cols="25% 75%", gap="8px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, art_type)
                    with g.cell():
                        st_write(bs.table_txt, preview_format)
