"""Slide — Step 0: A Real Example."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Step 0 filled example slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label

bs = BlockStyles

_PROJECT_MDC = """\
---
description: CalcApp budget tracker project rules
globs: ["**/*"]
alwaysApply: true
---
# Project: CalcApp — Personal Finance Tracker

## Context
React + TypeScript webapp for tracking personal expenses.
Target: mobile-first responsive, offline-capable (localStorage).

## Tech Stack
- React 19 + TypeScript 5.9 + Vite 7
- Vitest + Testing Library + vitest-axe
- React Router 7 + useReducer for state

## Quality Rules
- Every FR must have acceptance tests (Given/When/Then)
- WCAG 2.1 AA accessibility minimum
- All components must handle loading + error states
- No hardcoded strings — use constants file

## Naming: Components PascalCase, files kebab-case"""


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Step 0: A Real Example", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(
            bs.body,
            (bs.label, "Filled .cursor/rules/project.mdc"),
            " for a React budget tracker:",
        )
        st_space("v", 0.5)

        st_code(s.none, code=_PROJECT_MDC, language="markdown")
