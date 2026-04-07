"""Slide — Example: FR-001 in Full Detail."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """FR example slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label

bs = BlockStyles

_FR001 = """\
## FR-001: Edit Existing Expense

**User Story**: As a user, I want to edit an existing expense
so that I can correct mistakes.

**Acceptance Criteria**:
- Given an expense exists
  When I click the edit button
  Then a pre-filled form appears

- Given I am editing an expense
  When I modify fields and click Save
  Then the expense is updated in the list

- Given I am editing
  When I click Cancel
  Then no changes are saved

**Priority**: Must (MoSCoW)
**Test file**: tests/acceptance/fr-001-edit-expense.test.tsx"""


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Example: FR-001 in Full Detail", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(bs.body, (bs.label, "Complete functional requirement"), " with traceability:")
        st_space("v", 0.5)

        st_code(s.none, code=_FR001, language="markdown")
