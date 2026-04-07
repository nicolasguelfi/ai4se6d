"""Slide — Example: NFR-002 Accessibility."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


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
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Example: NFR-002 Accessibility", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(bs.body, (bs.label, "Complete non-functional requirement"), " with verification:")
        st_space("v", 0.5)

        st_code(s.none, code=_NFR002, language="markdown")
