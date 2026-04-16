"""Slide — Example: FR-001 in Full Detail."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
    st_marker("FR-001: Given/When/Then")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Example: FR-001 in Full Detail", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="FR-001 and GSE-One Principles",
            entries=[
                ("GSE-One principle", "Structured requirements with acceptance criteria -- output of /gse:assess."),
                ("Traceability", "Each FR links to user story, acceptance criteria, priority, and test file."),
                ("Given/When/Then", "Acceptance criteria use BDD format for unambiguous verification."),
                ("MoSCoW priority", "Prioritization ensures the /gse:plan phase sequences work correctly."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 0.5)

        with st_zoom(120):
            st_write(bs.body, (bs.label, "Complete functional requirement"), " with traceability:")
            st_space("v", 0.5)

            st_code(s.none, code=_FR001, language="markdown")
