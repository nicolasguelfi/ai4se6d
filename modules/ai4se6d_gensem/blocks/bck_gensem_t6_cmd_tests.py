"""Slide — /gse:tests: test strategy, execution, and evidence."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t6ct_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t6ct_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t6ct_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles

_TEST_TYPES = [
    ("Unit", "Individual functions in isolation", "DES, code"),
    ("Integration", "Modules working together", "DES, REQ"),
    ("E2E", "Complete user workflows", "REQ (stories)"),
    ("Acceptance", "Requirement met (user view)", "REQ (criteria)"),
    ("Visual", "UI rendering (screenshots)", "REQ (UI)"),
    ("Regression", "Previously fixed bugs", "RVW"),
]


def build():
    st_marker("/gse:tests")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:tests \u2014 How Do We Verify?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:tests \u2014 Full Testing Lifecycle",
                entries=[
                    ("Strategy", "Define test types, distribution (pyramid calibrated by domain), and risk-based prioritization."),
                    ("Environment", "Auto-detect framework from package manifest, install as dev dependency (pytest, vitest, etc.), configure runner."),
                    ("Visual testing", "For web/mobile: optional Playwright setup with screenshots, video on failure, visual regression."),
                    ("Evidence", "Test results, coverage, screenshots saved to tests/evidence/sprint-NN/TASK-NNN/. Campaign report in report.md."),
                    ("Cross-sprint regression", "Full test suite runs during /gse:review. Tests that passed last sprint but fail now \u2192 [REGRESSION] HIGH."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(85):
            with st_grid(cols="20% 45% 35%", gap="8px", cell_styles=_hdr_cell) as g:
                with g.cell():
                    st_write(bs.table_hdr, "Type")
                with g.cell():
                    st_write(bs.table_hdr, "Purpose")
                with g.cell():
                    st_write(bs.table_hdr, "Traces To")

            for test_type, purpose, traces in _TEST_TYPES:
                with st_grid(cols="20% 45% 35%", gap="8px", cell_styles=_normal_cell) as g:
                    with g.cell():
                        st_write(bs.table_lbl, test_type)
                    with g.cell():
                        st_write(bs.table_txt, purpose)
                    with g.cell():
                        st_write(bs.table_txt, traces)

            st_space("v", 1)
            st_write(bs.accent, "Test pyramid calibrated by project domain \u2014 not one-size-fits-all.")
