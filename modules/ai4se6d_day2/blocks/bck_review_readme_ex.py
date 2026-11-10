"""Slide — Exercise — README 80/20."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Exercise — README 80/20 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_readme_ex_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_readme_ex_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_readme_ex_timer")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "review_readme_ex_done")
bs = BlockStyles


_README = """\
Write README.md for CalcApp: what it does and for whom, tech stack,
install and run, scripts, project structure, features. Use only the
code and @docs/plan.md as sources. Invent nothing."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Exercise — README 80/20', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '15:50 → 16:05 · 15 min', tag=t.div)
            st_code(s.none, code=_README, language='text', line_numbers=False, font_size="36pt")
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'Run every command in it: do they all work?')
                with l.item():
                    st_write(
                        bs.body,
                        'Add a ',
                        (bs.keyword, 'Why'),
                        ' section: 3 sentences only you could write',
                    )
                with l.item():
                    st_write(bs.body, 'Commit on ', (bs.cmd, 'fix/review'), ': ', (bs.cmd, 'docs: README'))
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    'the README works as written and ends with a Why section of your own.',
                )
