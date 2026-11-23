"""Slide — Reality check: Anthropic finding, Bain study, gala dinner pivot."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
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

_NOTES_PLACE = [
    ("The message", "Naive VibeCoding is not banned: it is the right tool at home — personal prototypes, throwaway "
                    "demos, learning, exploring an idea."),
    ("Where it is not", "Production, enterprise, regulated environments, shared code: there, someone else will run, "
                        "maintain or audit what was generated."),
    ("The gala dinner", "Cooking for yourself, you can improvise. A gala dinner for 200 guests, with individual dietary "
                        "requirements and the press in attendance, needs a menu, a plan and checks: that is engineering."),
    ("The idea", "The choice depends on the stakes, not on the tool: the same agent can serve both, used differently."),
    ("Link to the course", "Next: what practices remain essential — VibeEngineering and its six principles."),
    ("Ask the room", "« Your project at work: home kitchen or gala dinner? »"),
]

def build():
    # Slide 27 — Anthropic Finding
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    with st_zoom(80):   # one-line title (NG, 2026-11-23)
                        st_write(bs.heading+"zoom:1.3;", "What Can Actually Be Delegated?", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(
                        title="Anthropic internal study (Dec 2025)",
                        entries=[
                            (
                                "~60% of work",
                                "132 Anthropic engineers and researchers "
                                "self-report using Claude in about 60% of "
                                "their work.",
                            ),
                            (
                                "0\u201320% fully delegable",
                                "Most say they can 'fully delegate' only "
                                "0\u201320% of their work. The rest needs "
                                "active human oversight and validation.",
                            ),
                            (
                                "Caveat",
                                "Self-reported, by staff of an AI lab, with "
                                "possible selection bias \u2014 an upper bound "
                                "for most teams.",
                            ),
                            (
                                "Collaboration, not replacement",
                                "AI handles implementation while humans focus on "
                                "architecture, design, and strategic oversight. "
                                "The modern workflow is constant collaboration.",
                            ),
                        ],
                        position="left", width="50vw",
                    )
            st_space("v", 4)
            with st_zoom(50):
                st_write(
                    bs.body,
                    (bs.stat_big, "~60% of work with AI")
                )
            with st_zoom(50):
                st_write(
                    bs.body,
                        (bs.stat_warn, "0\u201320% fully delegable")
                )

            st_space("v", 2)
            with st_zoom(150):
                st_write(
                    bs.body,
                    "Most work still needs human judgment, review, and direction.",
                )
                # REF: https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
                st_write(bs.source, cite("anthropic-workstudy2025"))
            
    st_space("v", "15vh")
    st_slide_break()

    # Slide 28 — Bain Study
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell():
                    with st_zoom(80):   # one-line title (NG, 2026-11-23)
                        st_write(bs.heading+"zoom:1.3;", "New Tools -> New Processes", tag=t.div, toc_lvl="2")
                with h.cell():
                    st_hover_tooltip(
                        title="Bain Technology Report (Sept 2025)",
                        entries=[
                            (
                                "10\u201315% with tools alone",
                                "Teams using AI coding assistants see 10\u201315% "
                                "productivity gains, but the time saved is often not "
                                "reassigned to other work, so it rarely shows up as "
                                "faster delivery.",
                            ),
                            (
                                "25\u201330% with process redesign",
                                "Some companies report 25\u201330% boosts by "
                                "pairing GenAI with end-to-end process "
                                "transformation.",
                            ),
                            (
                                "Why the gap?",
                                "Writing and testing code is only ~25\u201335% "
                                "of the time from idea to launch. Making coding faster "
                                "just moves the queue to the slower steps (requirements, "
                                "review, QA, release): the whole process has to change.",
                            ),
                        ],
                        position="left", width="50vw",
                    )
            st_space("v", 4)
            with st_zoom(40):
                st_write(
                    bs.body,
                    (bs.stat_warn, "10\u201315% with AI assistants alone"),
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
                # title and « i » on the same line (NG, 2026-11-23)
                with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                    with h.cell(), st_zoom(75):
                        st_write(bs.heading+"zoom:1.3;", "It Has Its Place", tag=t.div, toc_lvl="2")
                    with h.cell():
                        st_hover_tooltip(title="Trainer notes — It Has Its Place", entries=_NOTES_PLACE,
                                         position="left", width="50vw")
                st_space("v", 3)
                st_write(
                    bs.body,
                    (bs.keyword_ok, "At home: "),
                    "personal prototypes, throwaway demos, learning, exploring ideas.",
                )
                st_space("v", "2vh")
                st_write(
                    bs.body,
                    (bs.keyword_warn, "Not for: "),
                    "production, enterprise, regulated environments, shared code.",
                )
                st_space("v", 2)
                st_write(
                    bs.emphasis+s.project.colors.muted,
                    "A gala dinner for 200 guests. "
                    "Individual dietary requirements. Press in attendance. "
                    "Would you cook the same way?",
                )
