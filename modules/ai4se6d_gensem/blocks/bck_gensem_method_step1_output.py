"""Slide — Step 1: Example Output."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Step 1 output example slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label

bs = BlockStyles

_REQUIREMENTS = """\
# Requirements — [Your Project]

## Functional Requirements

### FR-001: User Authentication
As a user, I want to log in with email/password.
- Given valid credentials → redirect to dashboard
- Given invalid credentials → show error message

### FR-002: Dashboard Overview
As a user, I want to see my expense summary.
- Given expenses exist → show total, monthly breakdown
- Given no expenses → show empty state with CTA

### FR-003: Add Expense
As a user, I want to add a new expense.
- Given I fill all required fields → expense saved
- Given missing fields → validation errors shown"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Step 1: Example Output", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(bs.body, (bs.label, "Example requirements.md"), " with 3 FRs:")
        st_space("v", 0.5)

        st_code(s.none, code=_REQUIREMENTS, language="markdown")
