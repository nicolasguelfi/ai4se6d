"""Slide — Example: NFR-002 Accessibility."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """NFR example slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label

bs = BlockStyles

_NFR002 = """\
## NFR-002: Accessible Form Labels

**Requirement**: All form inputs must have associated
labels with proper ARIA attributes.

**Standard**: WCAG 2.1 AA

**Measurement**: 100% of inputs have aria-label
or associated <label> element.

**Verification**: Automated vitest-axe scan.

**Test file**: tests/nonfunctional/nfr-002-accessibility.test.tsx"""


def build():
    st_marker("NFR-002: WCAG Accessibility")
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Example: NFR-002 Accessibility", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="NFR-002 and GSE-One Principles",
            entries=[
                ("GSE-One principle", "Non-functional requirements with measurable criteria -- output of /gse:assess."),
                ("Standard reference", "Links to WCAG 2.1 AA -- external standard as verification anchor."),
                ("Measurement", "100% of inputs must have aria-label or associated label element."),
                ("Verification", "Automated vitest-axe scan -- fits into /gse:review automated checks."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 0.5)

        with st_zoom(120):
            st_write(bs.body, (bs.label, "Complete non-functional requirement"), " with verification:")
            st_space("v", 0.5)

            st_code(s.none, code=_NFR002, language="markdown")
