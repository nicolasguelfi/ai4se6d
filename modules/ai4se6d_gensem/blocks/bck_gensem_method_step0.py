"""Slide — Step 0: Seed - The Foundation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Step 0 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

_TEMPLATE = """\
---
description: Project rules for [Your Project Name]
globs: ["**/*"]
alwaysApply: true
---
# Project: [Name]
## Context
[1 paragraph: what, who, constraints]
## Tech Stack
- Frontend: [React/Vue] + TypeScript
- Testing: [Vitest/Jest]
## Quality Rules
- All features must have acceptance tests
- Accessibility: WCAG 2.1 AA minimum
## Naming Conventions
- Components: PascalCase
- Files: kebab-case"""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Step 0: Seed \u2014 The Foundation", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, (bs.label, "Template: "), ".cursor/rules/project.mdc")
        st_space("v", 0.5)

        st_code(s.none, code=_TEMPLATE, language="markdown")

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "This file constrains ALL subsequent AI interactions. "
                "It\u2019s your contract.",
            )
