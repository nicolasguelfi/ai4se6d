"""Slide — Step 3: Iterate - The Development Loop."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Step 3 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
    warning = Style.create(
        s.project.titles.body + s.project.colors.highlight + s.bold,
        "gs_step3_warning",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Step 3: Iterate \u2014 The Development Loop", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, "For ", (bs.keyword, "each FR"), ", follow these 5 sub-steps:")
        st_space("v", 0.5)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
            with l.item():
                st_write(bs.body, (bs.keyword, "Plan Mode \u2014 Test First: "), "write acceptance tests for this FR")
            with l.item():
                st_write(bs.body, (bs.keyword, "Act Mode \u2014 Implement: "), "make tests pass")
            with l.item():
                st_write(bs.body, (bs.keyword, "Verify: "), "run tests, check output")
            with l.item():
                st_write(bs.body, (bs.keyword, "Commit: "), 'git commit -m "feat(FR-00X): [description]"')
            with l.item():
                st_write(bs.body, (bs.keyword, "Update todo: "), "check off FR in Cursor todo list")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "Discipline: One FR per cycle. Never skip tests. "
                "Never 2 FRs at once. Stuck > 15 min? Simplify and move on.",
            )

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.warning,
                'Anti-pattern: "Implement all features" in one prompt = VibeCoding trap.',
            )
