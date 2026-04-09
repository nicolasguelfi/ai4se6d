"""Slide — Reality check: Anthropic finding, Bain study, gala dinner pivot."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Reality check slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    stat_big = s.project.titles.stat_hero_primary
    stat_warn = s.project.titles.stat_hero
    body = s.project.titles.body + s.center_txt
    source = s.project.citation + s.large + s.center_txt
    keyword_ok = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.bold + s.italic + s.project.colors.highlight + s.center_txt,
        "vc_reality_emphasis",
    )
bs = BlockStyles

def build():
    # Slide 27 — Anthropic Finding
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            with st_zoom(105):
                st_write(bs.heading, "What Can Actually Be Delegated?", tag=t.div, toc_lvl="1")
            st_space("v", 4)
            with st_grid(
                cols="95fr 5fr",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as sg:
                with sg.cell():
                    with st_zoom(50):
                        st_write(
                            bs.body,
                            (bs.stat_big, "60% integrable")
                        )
                with sg.cell():
                    st_hover_tooltip(
                        title="Anthropic Agentic Coding Report (2026)",
                        entries=[
                            (
                                "60% integrable",
                                "Developers report using AI in roughly 60% of "
                                "their work \u2014 code generation, documentation, "
                                "test writing, debugging assistance.",
                            ),
                            (
                                "0\u201320% fully delegable",
                                "Only 0 to 20% of tasks can be fully delegated "
                                "to AI without human review. The rest requires "
                                "active oversight: architecture, design decisions, "
                                "strategic choices.",
                            ),
                            (
                                "Collaboration, not replacement",
                                "AI handles implementation while humans focus on "
                                "architecture, design, and strategic oversight. "
                                "The modern workflow is constant collaboration.",
                            ),
                        ],
                        scale="2.2vw",
                        width="70vw",
                        position="left",
                    )
            with st_zoom(50):
                st_write(
                    bs.body,
                        (bs.stat_warn, "0\u201320% fully delegable")
                )

            st_space("v", 2)
            with st_zoom(170):
                st_write(
                    bs.body,
                    "Most work still needs human judgment, review, and direction.",
                )
                # REF: https://www.anthropic.com/research/impact-software-development
                st_write(bs.source, cite("anthropic-agentic2026"))
            
    st_space("v", "15vh")
    st_slide_break()

    # Slide 28 — Bain Study
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            with st_zoom(120):
                st_write(bs.heading, "New Tools -> New Processes", tag=t.div, toc_lvl="2")
            st_space("v", 4)
            with st_grid(
                cols="95fr 5fr",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as sg:
                with sg.cell():
                    with st_zoom(40):
                        st_write(
                            bs.body,
                            (bs.stat_warn, "10% gains without process change"),
                        )
                with sg.cell():
                    st_hover_tooltip(
                        title="Bain Technology Report (2025)",
                        entries=[
                            (
                                "10% with tools alone",
                                "AI coding tools deliver only 10\u201315% productivity "
                                "gains when deployed in isolation, without changing "
                                "existing workflows.",
                            ),
                            (
                                "25\u201330% with process redesign",
                                "Companies that pair AI with end-to-end process "
                                "transformation report 25\u201330% productivity boosts "
                                "\u2014 3x more than tools alone.",
                            ),
                            (
                                "Why the gap?",
                                "Writing code is only 25\u201335% of the development "
                                "lifecycle. Accelerating coding without redesigning "
                                "review, testing, and deployment creates new "
                                "bottlenecks, not breakthroughs.",
                            ),
                        ],
                        scale="2.2vw",
                        width="70vw",
                        position="left",
                    )
            with st_zoom(40):
                st_write(
                    bs.body,
                    (bs.stat_big, "25\u201330% with end-to-end process redesign"),
                )

            st_space("v", 2)
            with st_zoom(170):
                st_write(
                    bs.body,
                    "Tools alone are not enough.",
                )
                # REF: https://www.bain.com/insights/topics/technology-report/
                st_write(bs.source, cite("bain2025"))

    st_space("v", "20vh")
    st_slide_break()

    # Slide 29 — Naive VibeCoding Has Its Place (gala dinner pivot)
    with st_block(s.project.containers.page_fill_center_noalign):
        with st_zoom(110):
            with st_block(s.center_txt):
                st_write(bs.heading, "It Has Its Place", tag=t.div, toc_lvl="2")
                st_space("v", 1)
                st_write(
                    bs.body,
                    (bs.keyword_ok, "At home: "),
                    "personal prototypes, throwaway demos, learning, exploring ideas.",
                )
                st_space("v", 1)
                st_write(
                    bs.body,
                    (bs.keyword_warn, "Not for: "),
                    "production, enterprise, regulated environments, shared code.",
                )
                st_space("v", 2)
                st_write(
                    bs.emphasis,
                    "A gala dinner for 200 guests. "
                    "Individual dietary requirements. Press in attendance. "
                    "Would you cook the same way?",
                )
