"""Slide — Try it: Git on the CalcApp starter (steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Exercise steps styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_git_ex_timer")
bs = BlockStyles

_STEPS = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp
cd ~/ai4se/calcapp && git checkout -b mywork j2-start && npm ci
npm run test:run            # all green?
git switch -c feat/hello
# change one line of README.md, then:
git status && git diff
git add README.md && git commit -m "docs: say hello"
# break a file in src/ on purpose, look at git diff, then:
git restore <that-file> && npm run test:run"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Try it: Git on CalcApp", tag=t.div, toc_lvl="+1")
        st_write(bs.timer, "15 min — in a terminal", tag=t.div)
        st_write(
            bs.body,
            (bs.label, "Goal: "),
            "commit on a branch, break, restore.",
            tag=t.div,
        )
        st_code(s.none, code=_STEPS, language="bash", line_numbers=False, font_size="24pt")
