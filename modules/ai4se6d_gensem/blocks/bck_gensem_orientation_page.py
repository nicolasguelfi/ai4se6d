"""Slide — The printed orientation page: front "where am I?", back "when the agent drifts" (P12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Orientation page styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    item = s.project.titles.table_cell
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "orientation_cmd")
    card = Style.create(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md, "orientation_card")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "orientation_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "Your Orientation Page", tag=t.div, toc_lvl="+1", label="Orientation page")
            with st_grid(cols="repeat(auto-fit, minmax(460px, 1fr))", gap="24px", cell_styles=bs.card) as g:
                with g.cell():
                    st_write(bs.label, "Front — where am I?", tag=t.div)
                    with st_list(l_style=bs.item, li_style=bs.item, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.item, "The activities, in order, from plan to capitalisation")
                        with l.item(): st_write(bs.item, "Lost? ", (bs.cmd, "/gse-status"))
                        with l.item(): st_write(bs.item, "A sprint ends after delivery, then capitalisation")
                        with l.item(): st_write(bs.item, "CalcApp in Full mode, your mini-project in Lightweight")
                        with l.item(): st_write(bs.item, "One command form in opencode: ", (bs.cmd, "/gse-…"))
                with g.cell():
                    st_write(bs.label, "Back — when the agent drifts", tag=t.div)
                    with st_list(l_style=bs.item, li_style=bs.item, list_type=lt.ordered) as l:
                        with l.item(): st_write(bs.item, "Stop and discuss: ask why")
                        with l.item(): st_write(bs.item, (bs.cmd, "/gse-status"), ": where are we?")
                        with l.item(): st_write(bs.item, "Refuse the change")
                        with l.item(): st_write(bs.item, (bs.cmd, "/gse-pause"), ", then ", (bs.cmd, "/gse-resume"))
                        with l.item(): st_write(bs.item, "Go back to a safety tag ", (bs.cmd, "gse-backup/…"))
                        with l.item(): st_write(bs.item, "Call the trainer")
            st_write(bs.foot, "Printed and handed out now. Also in your kit: syllabus/orientation.md.", tag=t.div)
