"""Slide — Exercise — ship v0.1 (merge, tag, then main takes mywork)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise — ship v0.1 (merge and tag) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "ship_release_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "ship_release_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "ship_release_timer")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "ship_release_done")
bs = BlockStyles

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "ship_release_left")

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Exercise 16:15 → 16:30: merge, run the tests, tag v0.1, move "
     "main; wait until all see v0.1 in git tag."),
    ("The message",
     "15 minutes to ship v0.1: all the green work on your main line, tagged v0.1."),
    ("The commands",
     "On mywork, merge fix/review (and any finished feat/ branch), run the tests — fix before tagging if one is "
     "red —, tag v0.1, then move main onto mywork with git switch -C main mywork."),
    ("Why main",
     "From tomorrow, the methodology plugin treats main as the reference. Until now main held only the starter."),
    ("The expected warning",
     "Git says main and origin/main have diverged. That is normal: origin is the starter. Do not pull; you push "
     "to your own repository tomorrow morning."),
    ("If stuck",
     "Tutor window first; else the recovery tag j2-v0.1, then git tag v0.1 on it; else raise your hand."),
]


_SHIP = """\
git switch mywork
git merge fix/review          # + any finished feat/ branch not merged yet
npm run test:run              # all green? if not, fix before tagging
git tag v0.1
git switch -C main mywork     # main = your v0.1 (it held only the starter)
git log --oneline --graph --decorate -10"""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(55):
                st_write(bs.heading, 'Exercise — Ship v0.1', tag=t.div, toc_lvl='1', label='Ship v0.1 (16:15)')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — Ship v0.1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(70):
            st_write(bs.timer, '16:15 → 16:30 · 15 min', tag=t.div)
        with st_zoom(80), st_block(_left):
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'all green work on your main line, tagged ',
                (bs.cmd, 'v0.1'),
                '.',
                tag=t.div,
            )
            st_code(s.none, code=_SHIP, language='bash', line_numbers=False, font_size="36pt")
            st_write(
                bs.body,
                (bs.label, 'Why main: '),
                'from tomorrow, the methodology plugin treats ',
                (bs.cmd, 'main'),
                ' as the reference. Git says main and origin/main have diverged: normal, do not pull'
                ' (origin is the starter); you push to your own repository tomorrow morning.',
                tag=t.div,
            )
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    (bs.cmd, 'git tag'),
                    ' lists ',
                    (bs.cmd, 'v0.1'),
                    ', on a commit where the tests are green, and ',
                    (bs.cmd, 'main'),
                    ' is on that same commit (',
                    (bs.cmd, 'git branch -v'),
                    ').',
                )
            st_write(
                bs.body,
                (bs.label, 'If stuck: '),
                '1. ',
                'your tutor window',
                '  2. tag ',
                (bs.cmd, 'j2-v0.1'),
                ', then ',
                (bs.cmd, 'git tag v0.1'),
                ' on it  3. raise your hand',
                tag=t.div,
            )
