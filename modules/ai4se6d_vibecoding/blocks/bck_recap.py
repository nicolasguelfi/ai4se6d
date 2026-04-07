"""Slide — Closing recap: GenAI + VibeCoding takeaways, roadmap, key message."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Recap slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large
    transition = Style.create(
        s.Large + s.project.colors.accent + s.center_txt,
        "recap_transition",
    )
    keymsg = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.primary,
        "recap_keymsg",
    )
    closing_sub = Style.create(
        s.Large + s.italic + s.center_txt + s.project.colors.muted,
        "recap_closing_sub",
    )
bs = BlockStyles

def build():
    # Sub-slide 1: Recap GenAI
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Recap: Generative AI", tag=t.div, toc_lvl="1")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "GenAI = next-token prediction"), " at massive scale")
                with l.item(): st_write(bs.body, (bs.keyword, "Powerful"), " \u2014 code, text, images, reasoning")
                with l.item(): st_write(bs.body, (bs.keyword_warn, "Limited"), " \u2014 hallucinations, no real understanding")
                with l.item():
                    st_write(bs.body, (bs.keyword_accent, "84% adoption"), " among developers")
                    # REF: stackoverflow-survey2025
                    st_write(bs.source, cite("stackoverflow-survey2025"))

    st_slide_break()

    # Sub-slide 2: Recap VibeCoding to VibeEngineering
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Recap: VibeCoding \u2192 VibeEngineering", tag=t.div, toc_lvl="2")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "VibeCoding = fast"), " \u2014 describe, generate, ship")
                with l.item(): st_write(bs.body, (bs.keyword_warn, "Naive = dangerous"), " \u2014 vulnerabilities, debt, hallucinations")
                with l.item(): st_write(bs.body, (bs.keyword_accent, "VibeEngineering = discipline"), " \u2014 requirements, tests, review")
                with l.item(): st_write(bs.body, (bs.keyword, "Choose your level"), " \u2014 context determines the right approach")

    st_slide_break()

    # Sub-slide 3: The Road Ahead
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Road Ahead", tag=t.div, toc_lvl="2")

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Day 1\u20132"), " \u2014 Fundamentals + VibeCoding/VibeEngineering + Cursor")
                with l.item(): st_write(bs.body, (bs.keyword_accent, "Day 3\u20134"), " \u2014 SE Foundations for Generative SE")
                with l.item(): st_write(bs.body, (bs.keyword, "Day 5\u20136"), " \u2014 Mini-project + Ethics + Presentations")

            st_space("v", 1)
            st_write(
                bs.transition,
                "Next sessions: Requirements, V&V, NFRs",
                tag=t.div,
            )
            st_write(
                bs.body,
                "Traditional SE activities adapted to generative workflows:",
                tag=t.div,
            )
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, (bs.keyword, "Requirements elicitation"), " \u2014 methods for AI-augmented projects")
                with l.item(): st_write(bs.body, (bs.keyword, "Non-functional requirements"), " \u2014 quality, security, performance")
                with l.item(): st_write(bs.body, (bs.keyword, "Verification & Validation"), " \u2014 how to verify AI-generated code")

    st_slide_break()

    # Sub-slide 4: Key message centered (kitchen metaphor closing)
    with st_block(s.project.containers.page_fill_center):
        st_write(
            bs.keymsg,
            "Same Kitchen, Different Discipline",
            tag=t.div,
            toc_lvl="2",
        )
        st_space("v", 2)
        st_write(
            bs.closing_sub,
            "Same ingredients. Same utensils. The difference: the discipline of the chef.",
        )
