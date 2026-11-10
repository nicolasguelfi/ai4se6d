"""Slide — The oracle problem when the agent writes both code and tests (CCSET12, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Oracle problem styles."""
    heading = s.project.titles.heading
    callout = Style.create(s.project.titles.body + s.center_txt, "oracle_callout")
    body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Who Says What Is Correct?", tag=t.div, toc_lvl="+1", label="The oracle problem")
            with st_block(s.project.containers.callout):
                st_write(bs.callout, "A test needs an oracle: the expected result. "
                         "If the agent reads its own code to write it, the test copies the bug.", tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Take expected results from the requirements, not from the code")
                with l.item(): st_write(bs.body, "Write or read the test before the code (day 2: red, then green)")
                with l.item(): st_write(bs.body, "Check a test can fail: the mutant trick")
            st_write(bs.source, cite("barr-oracle2015"), " · ", cite("wang-llm-testing2025"), tag=t.div)
