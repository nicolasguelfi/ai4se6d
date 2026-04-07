"""Slide — Brainstorm: The Artifact."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Brainstorm artifact slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label

bs = BlockStyles

_BRAINSTORM = """\
# Brainstorm: Budget Alerts Feature

## Requirements Clarified
- Alert when spending exceeds 80% of monthly budget
- Notification via in-app banner (not email)

## Edge Cases Identified
- Multiple budgets per category
- Currency conversion for travel expenses

## Architecture Options
| Option | Pros | Cons |
|--------|------|------|
| Polling | Simple | Battery drain |
| Event-driven | Efficient | Complex setup |

## Risks
- API rate limits on currency service"""


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Brainstorm: The Artifact", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(bs.body, (bs.label, "Example output"), " from a brainstorm phase:")
        st_space("v", 0.5)

        st_code(s.none, code=_BRAINSTORM, language="markdown")
