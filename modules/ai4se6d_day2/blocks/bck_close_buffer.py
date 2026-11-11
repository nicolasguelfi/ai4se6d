"""Slide — Buffer — catch up, questions, tutor window."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Buffer — catch up, questions, tutor window — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "close_buffer_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "close_buffer_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "close_buffer_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Buffer: Catch Up, Ask, Tutor Window', tag=t.div, toc_lvl='1', label='Buffer (17:00)')
            st_write(bs.timer, '17:00 → 17:30', tag=t.div)
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Finish the exercise you missed (its sheet is in these slides)')
                with l.item():
                    st_write(bs.body, 'Questions to the trainer')
                with l.item():
                    st_write(bs.body, 'Your tutor window', " for anything about today's steps")
                with l.item():
                    st_write(
                        bs.body,
                        'Feedback: an issue on ',
                        (bs.cmd, 'nicolasguelfi/gensem'),
                        ', label ',
                        (bs.cmd, 'ai4se-ed2'),
                        ' — public, no confidential data',
                    )
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    'Before leaving: ',
                    (bs.cmd, 'git status'),
                    ' clean and ',
                    (bs.cmd, 'git tag'),
                    ' shows ',
                    (bs.cmd, 'v0.1'),
                    '; ',
                    (bs.cmd, 'git branch -v'),
                    ': ',
                    (bs.cmd, 'main'),
                    ' and ',
                    (bs.cmd, 'mywork'),
                    ' on the same commit.',
                )
