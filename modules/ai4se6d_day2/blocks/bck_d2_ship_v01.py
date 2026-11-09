"""Slide — Exercise — ship v0.1 (merge and tag)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Exercise — ship v0.1 (merge and tag) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_ship_v01_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_ship_v01_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_ship_v01_timer")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "d2_ship_v01_done")
bs = BlockStyles


_SHIP = """\
git switch mywork
git merge fix/review          # + any finished feat/ branch not merged yet
npx vitest run                # all green? if not, fix before tagging
git tag v0.1
git log --oneline --graph --decorate -10"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Exercise — Ship v0.1', tag=t.div, toc_lvl='1', label='Ship v0.1 (16:15)')
            st_write(bs.timer, '16:15 → 16:30 · 15 min', tag=t.div)
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'all green work on your main line, tagged ',
                (bs.cmd, 'v0.1'),
                '.',
                tag=t.div,
            )
            st_code(s.none, code=_SHIP, language='bash', line_numbers=False, font_size="36pt")
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    (bs.cmd, 'git tag'),
                    ' lists ',
                    (bs.cmd, 'v0.1'),
                    ', on a commit where the tests are green.',
                )
            st_write(
                bs.body,
                (bs.label, 'If stuck: '),
                '1. ',
                (bs.cmd, '@tutor'),
                '  2. tag ',
                (bs.cmd, 'j2-v0.1'),
                ', then ',
                (bs.cmd, 'git tag v0.1'),
                ' on it  3. raise your hand',
                tag=t.div,
            )
