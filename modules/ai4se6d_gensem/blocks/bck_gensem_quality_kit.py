"""Slide — Bring the quality kit (CI + coverage) into your CalcApp, at the start of day 4 (edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Quality kit styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "quality_kit_body")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "quality_kit_foot")
bs = BlockStyles

_KIT = (
    "git fetch origin --tags\n"
    "git checkout quality-kit -- .github/workflows/ci.yml\n"
    "npm install -D @vitest/coverage-v8@4.0.18\n"
    "npm pkg set scripts.test:coverage=\"vitest run --coverage\"\n"
    "git add .github package.json package-lock.json\n"
    "git commit -m \"ci: lint, tests with coverage, build\" && git push mine --all"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(72):
            st_write(bs.heading, "First: the Quality Kit", tag=t.div, toc_lvl="+1", label="Quality kit")
            st_write(bs.body, "From now on, every push runs lint, tests with coverage and the build on GitHub.", tag=t.div)
            with st_zoom(130):
                st_code(s.none, code=_KIT, language="bash", line_numbers=False)
            st_write(bs.foot, "You read the results at 11:45 (exercise E15).", tag=t.div)
