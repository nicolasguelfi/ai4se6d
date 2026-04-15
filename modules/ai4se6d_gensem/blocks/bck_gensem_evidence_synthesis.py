"""Slides — 3 Evidence Takeaways + Creativity homogenization warning."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: evidence-insight, transition-gse
# @reuse: bck_gensem_evidence_synthesis, human_creativity (v01)
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "synth_body")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "synth_acc",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt, "synth_hl",
    )
    label = Style.create(
        s.Large + s.bold + s.project.colors.primary, "synth_lbl",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    st_slide_break(marker_label="Evidence Synthesis")

    # ── Slide: 3 Takeaways ──────────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "Evidence Synthesis", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Evidence Synthesis — The full picture",
                        entries=[
                            ("3 experiments", "Three randomized controlled trials (Peng, Cui, METR) show gains ranging from +55% to -19% depending entirely on context, task, and expertise level."),
                            ("5 surveys, 95K+ devs", "84-85% use AI tools daily, but trust is dropping (29%) and 7h/week are lost to downstream problems AI creates."),
                            ("Enterprise data", "Bain and McKinsey confirm: tools alone yield ~10%. Adding structured process yields 25-30%. The method is the multiplier."),
                            ("The bottom line", "AI works. But without methodology, gains are captured only by experts, and hidden costs eat the benefits."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 2)

            with st_zoom(110):
                with st_list(li_style=bs.body) as l:
                    with l.item():
                        st_write(
                            bs.body,
                            (bs.label, "1. Gains are real but variable "),
                            (bs.body, "— depends on experience, context, task complexity"),
                        )
                    with l.item():
                        st_write(
                            bs.body,
                            (bs.label, "2. The methodology is the multiplier "),
                            (bs.body, "— 10% with tools → 25-30% with process"),
                        )
                    with l.item():
                        st_write(
                            bs.body,
                            (bs.label, "3. Senior expertise + structured process "),
                            (bs.body, "= where the real value is captured"),
                        )

            st_space("v", 2)
            st_write(bs.highlight, "This is why we need GSE-One.")

    st_slide_break(marker_label="The Homogenization Effect")

    # ── Slide: Creativity homogenization ────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "The Homogenization Effect", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Homogenization — Why it's a hidden risk",
                        entries=[
                            ("What Xiao found", "In a longitudinal study, engineers increasingly consult AI instead of colleagues. Team knowledge-sharing dynamics are disrupted."),
                            ("TOSEM research", "Identified 5 interconnected themes showing that AI-assisted solutions converge toward similar patterns, reducing diversity of approaches."),
                            ("Beyond productivity", "This is not a speed problem — it's a creativity and knowledge problem. Teams lose the diversity of solutions that comes from different human perspectives."),
                            ("GSE-One response", "Principle P16 (Devil's Advocate) explicitly counters this by challenging assumptions and forcing consideration of alternatives."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 2)
            st_write(
                bs.accent,
                "AI-assisted solutions converge toward similar patterns.",
            )
            st_space("v", 2)
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body + s.center_txt,
                    "Engineers consult AI instead of colleagues. "
                    "Knowledge-sharing dynamics are disrupted.",
                )
                st_space("v", 0.5)
                st_write(bs.source, cite("xiao-longitudinal2025"))
