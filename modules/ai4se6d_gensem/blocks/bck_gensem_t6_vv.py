"""Slide — V&V: Verification & Validation — Two Disciplines."""
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
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t6vv_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t6vv_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t6vv_acc")
    label = Style.create(s.Large + s.bold + s.project.colors.primary + s.center_txt, "t6vv_lbl")
    slogan = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "t6vv_slogan")

bs = BlockStyles


def build():
    st_marker("Verification & Validation")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Verification & Validation \u2014 Two Disciplines", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="V&V in GSE-One",
                        entries=[
                            ("Verification", "Build the thing right. Check internal consistency against the design (DES-). Unit, Integration, and Visual tests."),
                            ("Validation", "Build the right thing. Check the product against user intent (REQ-). Acceptance and E2E tests."),
                            ("Why it matters", "Both are necessary. 80% code coverage with 0 requirement-coverage = a thing built right that nobody needs."),
                            ("Kind column", "The test-types table tags each type: verification / validation / both. Regression is 'both' because a regressed bug may concern either side."),
                            ("Traceability", "Verification tests trace to DES-; validation tests trace to REQ-. This is the backbone of P6."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

            with st_zoom(110):
                with st_grid(cols=s.project.containers.responsive_2col, gap="32px") as g:
                    with g.cell():
                        with st_block(_cell):
                            st_write(bs.label, "Verification")
                            st_space("v", 0.3)
                            st_write(bs.slogan, "Build the thing right.")
                            st_space("v", 0.5)
                            st_write(bs.body, (bs.keyword, "Trace: "), "DES- (design)")
                            st_write(bs.body, (bs.keyword, "Types: "), "Unit, Integration, Visual")
                            st_space("v", 0.5)
                            st_write(bs.body, "Does the code do what we designed?")
                    with g.cell():
                        with st_block(_cell_acc):
                            st_write(bs.label, "Validation")
                            st_space("v", 0.3)
                            st_write(bs.slogan, "Build the right thing.")
                            st_space("v", 0.5)
                            st_write(bs.body, (bs.keyword, "Trace: "), "REQ- (requirements)")
                            st_write(bs.body, (bs.keyword, "Types: "), "Acceptance, E2E")
                            st_space("v", 0.5)
                            st_write(bs.body, "Does the product solve the user's problem?")

                st_space("v", 1)
                st_write(bs.accent, "Regression covers both \u2014 a regressed behavior may be a design defect (verification) or a scope drift (validation).")
