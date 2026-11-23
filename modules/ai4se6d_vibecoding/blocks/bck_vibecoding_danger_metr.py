"""Slide — The METR Paradox: tasks took 19% longer with AI (early 2025) + Feb 2026 update."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """METR Paradox stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "vc_danger_metr_text_cell")

_PROMPT = (
    f"{_PREFIX} A brain split in two halves: left half is bright and optimistic with "
    "upward arrows in electric blue. Right half confronts a stopwatch showing delay "
    "in amber. A teal mirror between them reflects the disconnect. Symbolizes the gap "
    f"between perceived and actual AI productivity. {_SUFFIX}"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):   # one-line title
                    st_write(bs.heading+"zoom:1.3;", "The METR Paradox", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(
                        title="METR Study Details",
                        entries=[
                            (
                                "Study design",
                                "Randomized controlled trial (METR - Model Evaluation and Threat Research, July 2025). "
                                "Each task randomly allowed or disallowed AI. "
                                "16 devs, 246 real issues on mature open-source "
                                "repos they knew well (5 years on average).",
                            ),
                            (
                                "+19% time",
                                "Tasks took 19% longer with AI allowed "
                                "(95% CI: +2% to +39%). Time shifted to "
                                "prompting, waiting on and reviewing AI output.",
                            ),
                            (
                                "Reading « 95% CI: +2% to +39% »",
                                "For experienced developers working on their own projects, with early-2025 "
                                "tools, allowing AI increased task time on average by about 19%. This average "
                                "slowdown lies, with 95% reliability, between +2% and +39%. From one developer "
                                "to another, the effect varies much more.",
                            ),
                            (
                                "Why the range is wide",
                                "Only 16 developers, and task durations vary a lot (minutes to hours). "
                                "Fewer, noisier measurements give a wider interval. Compare the "
                                "Feb 2026 update below: its interval (−38% to +9%) crosses zero, "
                                "so it cannot tell faster from slower.",
                            ),
                            (
                                "Perception gap",
                                "Before: devs forecast a 24% speedup. "
                                "After: they still believed AI had sped them "
                                "up by 20%. Measured: 19% slower.",
                            ),
                            (
                                "<44% accepted",
                                "Developers accepted fewer than 44% of the "
                                "AI generations they reviewed.",
                            ),
                            (
                                "Tool used",
                                "Cursor Pro with Claude 3.5/3.7 Sonnet "
                                "\u2014 state-of-the-art AI coding tools "
                                "at the time of the study (early 2025).",
                            ),
                            (
                                "Feb 2026 update \u2014 the study",
                                "Follow-up started August 2025 with agentic tools (e.g. Claude Code, Codex): "
                                "57 developers, 143 repositories, 800+ tasks, same random \u00ab AI allowed / "
                                "disallowed \u00bb design. 10 developers came back from the first study; 47 were new, "
                                "from more diverse open-source projects.",
                            ),
                            (
                                "Feb 2026 update \u2014 the results",
                                "Returning developers: \u221218% time with AI (interval \u221238% to +9%). "
                                "New developers: \u22124% (interval \u221215% to +9%). Both intervals cross "
                                "zero: the best guess is now a speedup, but the data cannot rule out "
                                "\u00ab no effect \u00bb or a small slowdown.",
                            ),
                            (
                                "Feb 2026 update \u2014 why it is unreliable",
                                "Selection effects: many developers refused to take part because they no longer "
                                "want to work without AI, and 30\u201350% of participants did not submit some "
                                "tasks for the same reason. The tasks where AI helps most are missing, so the "
                                "measured speedup is likely an underestimate (METR: \u00ab likely a lower-bound \u00bb).",
                            ),
                            (
                                "Feb 2026 update \u2014 METR's conclusion",
                                "Developers are likely more sped up by AI now than in early 2025, but the data is "
                                "\u00ab only very weak evidence \u00bb of how much. METR is redesigning the study. "
                                "Say: \u00ab the 2025 slowdown is outdated; the size of today's gain is still unknown. \u00bb",
                            ),
                        ],
                        position="left", width="50vw",
                    )

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="3vw",
                cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_metr",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(96):   # text cell fills the slide (NG, 2026-11-23; 96 since the longer Feb 2026 line)
                        with st_zoom(60):
                            st_write(bs.stat, "+19%")
                        st_space("v", 0.5)
                        st_write(
                            bs.body,
                            "more time with AI \u2014 experienced devs, own repos, early 2025.",
                        )
                        st_space("v", 0.5)
                        st_write(
                            bs.body,
                            (bs.keyword, "Perception gap: "),
                            "forecast 24% faster; afterwards ",
                            (bs.keyword_warn, "still believed"),
                            " 20% faster.",
                        )
                        st_space("v", 0.5)
                        st_write(
                            bs.body,
                            (bs.keyword, "Feb 2026 update: "),
                            "with newer tools, AI now likely speeds developers up — but the gain "
                            "cannot yet be measured reliably.",
                        )
                        st_space("v", 0.5)
                        # REF: METR, arXiv 2507.09089, July 2025 + METR blog 2026-02-24
                        st_write(bs.source, cite("metr2025"), " · ", cite("metr-uplift2026"))
