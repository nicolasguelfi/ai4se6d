"""Slide — Steps 4-5: Review & Compound."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Steps 4-5 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
    closing = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_step45_closing",
    )
bs = BlockStyles

_REVIEW_PROMPT = """\
Review codebase against docs/requirements.md.
For each FR and NFR, classify as: satisfied / partial / missing.
Suggest fixes for partial and missing items."""

_EXAMPLE_RULES = """\
## New Rules (from CalcApp v0.3 iteration)
- Always seed DB with test data before integration tests
- Use custom hooks for shared state (no prop drilling)
- Test accessibility with vitest-axe on every component
- Keep API response types in a shared types/ directory
- Commit message format: feat(FR-XXX): description"""


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Steps 4\u20135: Review & Compound", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="32px",
        ) as g:
            with g.cell():
                st_write(bs.label, "Step 4 \u2014 Review", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, (bs.keyword, "Plan Mode prompt:"))
                st_code(s.none, code=_REVIEW_PROMPT, language="text")
                st_space("v", 0.5)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, "For each FR/NFR: ", (bs.keyword, "satisfied"), " / ", (bs.keyword, "partial"), " / ", (bs.keyword, "missing"))
                    with l.item():
                        st_write(bs.body, "Budget ", (bs.keyword, "30 min"), " for top-priority fixes")

            with g.cell():
                st_write(bs.label, "Step 5 \u2014 Compound", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, "Update .cursor/rules/project.mdc with 3\u20135 new rules:")
                st_space("v", 0.5)
                st_code(s.none, code=_EXAMPLE_RULES, language="markdown")

        st_space("v", 1)
        with st_block(s.center_txt):
            st_write(bs.closing, "These rules travel with you \u2014 copy to next project.")
