"""Slide — Real case: green tests, green review, red build (CCSET13, edition 2).

Source: reference rehearsal of days 1-4 (2026-11-10), exercise E15. The GitHub CI failed at the
build step (tsc type error in a test file) while `npm run test:run` and the 7-reviewer
`/gse-review` were green — Vitest runs the tests without type-checking.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Green tests / red build styles."""
    heading = s.project.titles.heading
    caption = Style.create(s.project.titles.caption + s.center_txt, "redbuild_caption")
    check = Style.create(s.project.titles.table_label + s.center_txt, "redbuild_check")
    green = Style.create(s.project.titles.table_cell + s.project.colors.success + s.bold + s.center_txt,
                         "redbuild_green")
    red = Style.create(s.project.titles.table_cell + s.project.colors.critical + s.bold + s.center_txt,
                       "redbuild_red")
    cell = Style.create(s.project.titles.table_cell + s.center_txt, "redbuild_cell")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "redbuild_cmd")
    body = s.project.titles.body
    lesson = Style.create(s.project.titles.body + s.bold + s.center_txt, "redbuild_lesson")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "redbuild_foot")
bs = BlockStyles

# (check, what it looked at, result, ok?)
ROWS = [
    ("Tests", "npm run test:run — runs the tests, skips type-checking", "green", True),
    ("Review", "/gse-review — 7 reviewers read the code", "passed", True),
    ("CI build", "tsc -b — compiles everything, test files included", "red", False),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(64):
            st_write(bs.heading, "Green Tests, Red Build", tag=t.div, toc_lvl="+1",
                     label="Real case — green tests, red build")
            st_write(bs.caption, "Real case — our rehearsal of this exercise, with the course model", tag=t.div)
            for check, what, result, ok in ROWS:
                with st_grid(cols="16% 64% 16%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.check, check)
                    with g.cell():
                        cmd, rest = what.split(" — ", 1)
                        st_write(bs.cell, (bs.cmd, cmd), " — " + rest)
                    with g.cell(): st_write(bs.green if ok else bs.red, result)
            st_write(bs.body, "The type error: ", (bs.cmd, "tests/policy/lint.test.ts"), " cannot find module ",
                     (bs.cmd, "node:child_process"), ". Coverage that evening: 99 % of statements.", tag=t.div)
            with st_block(s.project.containers.callout):
                st_write(bs.lesson, "Each check sees a different thing. Green tests ≠ green build.", tag=t.div)
            st_write(bs.foot, "The CI caught what the review missed (GSE-One fixed it later as RVW-033). "
                     "Before you say \"done\": npm run build.", tag=t.div)
