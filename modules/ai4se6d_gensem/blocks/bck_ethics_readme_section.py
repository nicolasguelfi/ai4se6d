"""Slide — The README section "Ethics and compliance" (exercise E23, edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Ethics README section styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "ethics_readme_body")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "ethics_readme_foot")
bs = BlockStyles

_SECTION = (
    "## Ethics and compliance\n"
    "- AI Act: <does the app use AI? risk level; how users are told>\n"
    "- Licences: <this repository's licence; dependencies checked; any doubt>\n"
    "- Secrets: <.env never committed; history checked on <date>>\n"
    "- Personal data: <which, where, why, how long — or \"none\">"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "Your README: Ethics and Compliance", tag=t.div, toc_lvl="+1",
                     label="README section — ethics and compliance")
            st_write(bs.body, "Four short answers. \"Not sure, because…\" is a valid answer.", tag=t.div)
            with st_zoom(120):
                st_code(s.none, code=_SECTION, language="markdown", line_numbers=False)
            st_write(bs.foot, "The first task of a new sprint: /gse-task, then /gse-deliver; then push.", tag=t.div)
