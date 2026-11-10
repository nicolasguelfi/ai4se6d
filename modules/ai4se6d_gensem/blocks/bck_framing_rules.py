"""Slide — Mini-project rules (decision P17, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Rules styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "rules_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "rules_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "The Rules", tag=t.div, toc_lvl="+1", label="Mini-project rules")
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Judged on the process, not on the size")
                with l.item(): st_write(bs.body, "A first sprint of 8-10 complexity points, in Lightweight mode")
                with l.item(): st_write(bs.body, "No multi-service infrastructure: one app")
                with l.item(): st_write(bs.body, "A deployable technology, or your own Dockerfile")
                with l.item(): st_write(bs.body, "An existing project? One small change, with ", (bs.cmd, "/gse-go --adopt"))
                with l.item(): st_write(bs.body, "Private repository allowed: no client code on a public one")
            st_write(bs.foot, "Demo on day 6: problem, product, one GSE-One moment, one lesson — 5 to 7 minutes.", tag=t.div)
