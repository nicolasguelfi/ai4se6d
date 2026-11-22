"""Slide — Hands-up quiz — answers."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Hands-up quiz — answers — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "bridge_quiz_answers_body")
    keyword = s.bold + s.project.colors.highlight
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Quiz — Answers', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, 'Yes'), ' — RED first is the normal start')
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, 'No'),
                        ' — golden rule: you review the test between RED and GREEN',
                    )
                with l.item():
                    st_write(bs.body, (bs.keyword, 'No'), ' — they prove nothing: fix the tests')
                with l.item():
                    st_write(bs.body, (bs.keyword, 'No'), ' — 200-400 lines per review: review per task')
                with l.item():
                    st_write(bs.body, (bs.keyword, 'Yes'), ' — with a written reason')
