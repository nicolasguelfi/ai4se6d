"""Slide — Logs: build log, runtime log, health check; healthy is not the right version (CCSET16, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Logs styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "deploy_logs_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "deploy_logs_tl")
    txt = s.project.titles.table_cell
    body = s.project.titles.body
    label = s.project.titles.label
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

ROWS = [
    ("Build log", "while the image is built", "an install, test or compile step that failed — day 4's CI again"),
    ("Runtime log", "while the container runs", "crashes, errors, the requests it received"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "Logs: What Really Happened", tag=t.div, toc_lvl="+1", label="Logs and health")
            with st_grid(cols="18% 26% 52%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Log")
                with g.cell(): st_write(bs.hdr, "Written")
                with g.cell(): st_write(bs.hdr, "Tells you")
            for name, when, what in ROWS:
                with st_grid(cols="18% 26% 52%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, when)
                    with g.cell(): st_write(bs.txt, what)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "The app writes to its standard output; the platform collects it")
                with l.item(): st_write(bs.body, "Read for the first error, not the last line")
                with l.item(): st_write(bs.body, (bs.label, "Health check"), ": an address the platform calls "
                                        "to know the container is alive")
                with l.item(): st_write(bs.body, (bs.label, "Healthy ≠ the right version"), ": compare the commit "
                                        "that is live with the one you pushed")
            st_write(bs.source, cite("wiggins-twelvefactor2011"), tag=t.div)
