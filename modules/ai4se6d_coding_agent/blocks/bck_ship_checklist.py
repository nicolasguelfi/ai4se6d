"""Slide — v0.1 — what you just built."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """v0.1 — what you just built — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "ship_checklist_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "ship_checklist_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ship_checklist_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'v0.1 — What You Just Built', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Two pages with navigation')
                with l.item():
                    st_write(bs.body, 'Add an expense — it survives a refresh')
                with l.item():
                    st_write(bs.body, '4+ tests, each written ', (bs.keyword, 'before'), ' its code')
                with l.item():
                    st_write(bs.body, 'A review: triage, fixes, one reasoned refusal')
                with l.item():
                    st_write(bs.body, 'A README with ', (bs.keyword, 'your'), ' Why')
                with l.item():
                    st_write(bs.body, 'A tag: ', (bs.cmd, 'v0.1'))
            st_write(bs.foot, 'You drove, the agent typed. That is VibeEngineering.', tag=t.div)
