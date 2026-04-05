"""Slide 34 — Claude Code: CLI-first, highest autonomy."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Claude Code slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.titles.caption
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A terminal window in electric blue with autonomous process flows running inside, "
    "branching decision trees in teal, completion in amber. "
    f"{_SUFFIX}"
)

def build():
    # Slide 1 — Claude Code overview
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Claude Code", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ide_claude_code",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Terminal CLI-first"), " \u2014 runs in your shell, not a GUI")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Highest autonomy"), " \u2014 agentic by design")
                        # REF: anthropic-claude-code2025
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "5 sub-agents"), " \u2014 concurrent autonomous workers")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Agent Teams"), " \u2014 multi-agent orchestration")
                        # REF: anthropic-claude-code2025
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "17 hooks"), " \u2014 lifecycle automation points")
                        # REF: awesome-claude-plugins2025
                        with l.item():
                            st_write(bs.body, (bs.keyword, "9000+ plugins"), " via MCP servers")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "Agent SDK"), " \u2014 build custom AI agents")

            st_write(bs.source, cite("anthropic-claude-code2025"), " \u00b7 ", cite("awesome-claude-plugins2025"))

    st_slide_break()

    # Slide 2 — Claude Code unique strengths
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Claude Code: Unique Strengths", tag=t.div, toc_lvl="2")
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Memory"), " \u2014 persistent context via CLAUDE.md files at project/user/global level")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "WebSearch"), " \u2014 real-time documentation and API lookups")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Permission System"), " \u2014 fine-grained control over tool access")
                with l.item():
                    st_write(bs.body, (bs.keyword, "IDE integrations"), " \u2014 VS Code, JetBrains, Neovim via extensions")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Pricing (Q1 2026)"), " \u2014 Max plan $100/month or API-based pay-per-use")

            st_write(bs.source, cite("anthropic-claude-code2025"), " \u00b7 ", cite("awesome-claude-plugins2025"))
