"""Slide — Catch-up — restart from tag j2-part1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Catch-up — restart from tag j2-part1 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_catchup_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_catchup_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_p2_catchup_foot")
bs = BlockStyles


_CATCHUP = """\
cd ~ && mv calcapp calcapp-old
git clone https://github.com/nicolasguelfi/calcapp-starter calcapp
cd calcapp && git checkout -b mywork j2-part1 && npm ci"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Catch-up: Tag j2-part1', tag=t.div, toc_lvl='+1')
            st_write(bs.body, 'Restart from the end of Part 1 (first features, tests green):', tag=t.div)
            st_code(s.none, code=_CATCHUP, language='bash', line_numbers=False, font_size="36pt")
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        'Copy back ',
                        (bs.cmd, 'docs/plan.md'),
                        ' and ',
                        (bs.cmd, 'AGENTS.md'),
                        ' from ',
                        (bs.cmd, 'calcapp-old'),
                    )
                with l.item():
                    st_write(bs.body, 'Skip the tasks already done in the tag, continue with the next one')
            st_write(bs.foot, 'A recovery tag is a safety net, not a failure.', tag=t.div)
