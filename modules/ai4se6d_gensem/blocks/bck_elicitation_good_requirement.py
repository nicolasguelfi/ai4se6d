"""Slide — What a good requirement is (ISO/IEC/IEEE 29148 characteristics) (CCSET10, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Good requirement styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "good_req_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "good_req_tl")
    bad = Style.create(s.project.titles.table_cell + s.project.colors.critical, "good_req_bad")
    good = Style.create(s.project.titles.table_cell + s.project.colors.success, "good_req_good")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

ROWS = [
    ("Unambiguous", "The list loads quickly", "The list of 1,000 expenses shows in under 200 ms"),
    ("Verifiable", "The app is easy to use", "A new user adds an expense in under 30 s, unaided"),
    ("Singular", "Add and edit expenses", "Add an expense · Edit an expense"),
    ("Necessary", "Export to 12 formats", "Export to CSV (the accountant asked for it)"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(65):
            st_write(bs.heading, "A Good Requirement", tag=t.div, toc_lvl="+1", label="Characteristics of a good requirement")
            with st_grid(cols="22% 36% 38%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Characteristic")
                with g.cell(): st_write(bs.hdr, "✗ Weak")
                with g.cell(): st_write(bs.hdr, "✓ Better")
            for name, weak, better in ROWS:
                with st_grid(cols="22% 36% 38%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.bad, weak)
                    with g.cell(): st_write(bs.good, better)
            st_write(bs.source, "Also: appropriate, complete, feasible, correct, conforming — ",
                     cite("iso29148-2018"), tag=t.div)
