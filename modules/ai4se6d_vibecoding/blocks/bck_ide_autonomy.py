"""Slide 32 — The Autonomy Spectrum + The Agentic Turn."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Autonomy spectrum slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    takeaway = s.project.titles.body + s.center_txt
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A steep upward curve in electric blue with inflection point in amber burst. "
    "Below: small tool icons. Above: larger autonomous agent icons rising. "
    f"{_SUFFIX}"
)

def build():
    # Slide 1 — The Autonomy Spectrum (Lines 455-461)
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Autonomy Spectrum", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item():
                    st_write(bs.body, (bs.keyword, "Passive assistance"), " — responds only when invoked")
                with l.item():
                    st_write(bs.body, (bs.keyword, "Proactive copiloting"), " — suggests unprompted, you decide")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "Task-level delegation"), " — you describe, AI executes")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Autonomous agents"), " — AI plans, executes, tests, iterates")
                with l.item():
                    st_write(bs.body, (bs.keyword_warn, "Multi-agent orchestration"), " — specialized AI teams collaborate")

    st_slide_break()

    # Slide 2 — The Agentic Turn
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.subheading, "The Agentic Turn", tag=t.div, toc_lvl="2")

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
                        name="ide_autonomy_agentic",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        # REF: opencode-sst2024
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "opencode"), " \u2014 plan, build, @subagents")
                        # REF: anthropic-claude-code2025
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Claude Code"), " \u2014 subagents, background tasks")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "GitHub Copilot"), " \u2014 issue \u2192 pull request")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Cursor"), " \u2014 IDE, CLI and cloud agents")
                    st_space("v", 1)
                    st_write(
                        bs.takeaway,
                        "It ", (bs.keyword_warn, "plans, edits, runs"),
                        ". You ", (bs.keyword_accent, "frame and review"), ".",
                    )

            st_write(bs.source, cite("opencode-sst2024"), " \u00b7 ", cite("anthropic-claude-code2025"))
