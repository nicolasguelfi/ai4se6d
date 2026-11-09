"""Slide — Post-lunch re-orientation checklist."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Post-lunch re-orientation checklist — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_reorient_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_reorient_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_p2_reorient_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Re-orientation (5 min)', tag=t.div, toc_lvl='+1')
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'cd calcapp'),
                        ' → ',
                        (bs.cmd, 'git status'),
                        ': clean, on ',
                        (bs.cmd, 'mywork'),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'npm test'),
                        ' → Part 1 tests still green (',
                        (bs.cmd, 'q'),
                        ' quits)',
                    )
                with l.item():
                    st_write(bs.body, (bs.cmd, 'npm run dev'), ' → the app renders in the browser')
                with l.item():
                    st_write(
                        bs.body,
                        'Start opencode, read ',
                        (bs.cmd, '@docs/plan.md'),
                        ': which task is next?',
                    )
            st_write(bs.foot, 'One check fails and you cannot fix it in 5 minutes? Next slide.', tag=t.div)
