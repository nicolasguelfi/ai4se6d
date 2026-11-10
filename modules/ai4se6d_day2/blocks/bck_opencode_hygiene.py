"""Slide — What NOT to put in the context."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Context hygiene styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    danger = Style.create(s.project.titles.keyword + s.project.colors.critical, "hyg_danger")
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "hyg_closing")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "What NOT to Put in Context", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, (bs.danger, "Secrets"), " — .env, your model key, passwords: never paste, never @")
            with l.item(): st_write(bs.body, (bs.keyword, "Generated folders"), " — node_modules/, dist/ stay in .gitignore")
            with l.item(): st_write(bs.body, (bs.keyword, "Whole logs"), " — paste the 10 lines that matter")
            with l.item(): st_write(bs.body, (bs.keyword, "Old tasks"), " — one task, one session: /new")
        st_space("v", 1)
        st_write(bs.closing, "Less but relevant beats more.", tag=t.div)
