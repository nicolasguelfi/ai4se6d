"""Slides — Framework landscape, key frameworks, synthesis, roadmap, → GSE-One."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: task-card, transition-gse
# @reuse: bck_gensem_fw_landscape, _synthesis, _roadmap, sota_takeaway (v01)
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top
_page_fill_center = s.project.containers.page_fill_center

_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell
_active_cell = s.project.containers.table_active_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "fw_body")
    body_c = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "fw_body_c")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "fw_acc",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt, "fw_hl",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.primary, "fw_kw",
    )
    stat = Style.create(
        s.Large + s.bold + s.project.colors.highlight, "fw_stat",
    )
    label = Style.create(
        s.Large + s.bold + s.project.colors.primary + s.center_txt, "fw_lbl",
    )
    cat_label = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt, "fw_cat",
    )
    source = s.project.citation + s.large + s.center_txt
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
    table_lbl_active = s.project.titles.table_label_active
bs = BlockStyles

# Category cell styles
_cat_adapt = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cat_native = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cat_plugin = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


def build():
    st_slide_break(marker_label="Methodological Frameworks")

    # ── Slide 1: The Landscape ──────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "The Methodological Landscape",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="3 Categories of GenSE Frameworks",
                entries=[
                    ("Adaptations", "Existing agile/DevOps methods extended with AI capabilities (AgileGen, Agentic DevOps). Familiar but limited."),
                    ("AI-Native", "Methods designed from scratch for AI-augmented development (SE 3.0, V-Bounce, Promptware, MAISTRO). Ambitious but mostly theoretical."),
                    ("Process Plugins", "Composable methodology plugins that work across tools (Compound Engineering → GSE-One). Practical and portable."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 2)

            # Row 1: Adaptations
            st_write(bs.cat_label, "Adaptations — Existing methods extended")
            st_space("v", 0.5)
            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="12px", cell_styles=_cat_adapt,
            ) as g:
                with g.cell():
                    st_write(bs.body_c, (bs.keyword, "AgileGen"), (bs.body, " — Gherkin + memory pool"))
                with g.cell():
                    st_write(bs.body_c, (bs.keyword, "Agentic DevOps"), (bs.body, " — Microsoft vision"))

            st_space("v", 1)

            # Row 2: AI-Native
            st_write(bs.cat_label, "AI-Native — Built for GenAI from scratch")
            st_space("v", 0.5)
            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="12px", cell_styles=_cat_native,
            ) as g:
                with g.cell():
                    st_write(bs.body_c, (bs.keyword, "SE 3.0"), (bs.body, " — intent-centric"))
                with g.cell():
                    st_write(bs.body_c, (bs.keyword, "V-Bounce"), (bs.body, " — V-model adapted"))
                with g.cell():
                    st_write(bs.body_c, (bs.keyword, "Promptware"), (bs.body, " — SE for prompts"))
                with g.cell():
                    st_write(bs.body_c, (bs.keyword, "MAISTRO"), (bs.body, " — 7-phase agile"))

            st_space("v", 1)

            # Row 3: Process Plugins
            st_write(bs.cat_label, "Process Plugins — Portable methodology")
            st_space("v", 0.5)
            with st_grid(
                cols="repeat(auto-fit, minmax(350px, 1fr))",
                gap="12px", cell_styles=_cat_plugin,
            ) as g:
                with g.cell():
                    st_write(bs.body_c, (bs.highlight, "Compound Engineering → GSE-One"))

    st_slide_break(marker_label="What's Missing Everywhere")

    # ── Slide 2: What's missing everywhere ──────────────────────────
    with st_block(_page_fill_center):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "What's Missing Everywhere",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="Gaps in Existing Frameworks",
                entries=[
                    ("Knowledge capitalization", "No framework except CE/GSE-One systematically captures learnings across development cycles."),
                    ("AI integrity", "No framework addresses hallucination detection, confidence levels, or adversarial self-review (P15-P16)."),
                    ("Adaptive communication", "No framework adapts its behavior to the developer's experience level (P9)."),
                    ("Cross-tool portability", "Most frameworks are locked to one IDE or tool."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            with st_zoom(120):
                st_space("v", 2)
                with st_grid(
                    cols="repeat(auto-fit, minmax(280px, 1fr))",
                    gap="24px",
                ) as g:
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "Knowledge Capitalization")
                            st_space("v", 0.5)
                            st_write(bs.body_c, "No compound phase")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "AI Integrity")
                            st_space("v", 0.5)
                            st_write(bs.body_c, "No P15-P16")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "Adaptive Communication")
                            st_space("v", 0.5)
                            st_write(bs.body_c, "No P9")
                    with g.cell():
                        with st_block(s.project.containers.callout):
                            st_write(bs.accent, "Cross-Tool Portability")
                            st_space("v", 0.5)
                            st_write(bs.body_c, "Locked to one IDE")

    st_slide_break(marker_label="Framework Comparison")

    # ── Slide 3: Comparison table ───────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "Framework Comparison",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="How to Read This Table",
                entries=[
                    ("Columns", "Practical (ready to use), Agile (iterative), Tool Support (IDE integration), Enterprise (scalable), Learning Curve (ease of adoption)."),
                    ("Symbols", "✓✓ = strong, ✓ = partial, ★ = weak or theoretical."),
                    ("Active row", "GSE-One (Compound Engineering) is highlighted as the most balanced across all criteria."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            _headers = ["Framework", "Practical", "Agile", "Tools", "Enterprise", "Learning"]
            _rows = [
                ("AgileGen", "\u2713", "\u2713\u2713", "\u2605", "\u2605", "Medium", False),
                ("Agentic DevOps", "\u2605", "\u2713", "\u2713\u2713", "\u2713\u2713", "High", False),
                ("SE 3.0", "\u2605", "\u2605", "\u2605", "\u2713", "High", False),
                ("V-Bounce", "\u2713", "\u2713", "\u2605", "\u2605", "Medium", False),
                ("Promptware", "\u2713\u2713", "\u2713", "\u2713", "\u2713", "Low", False),
                ("GSE-One", "\u2713\u2713", "\u2713\u2713", "\u2713\u2713", "\u2713\u2713", "Low", True),
            ]

            with st_grid(
                cols="repeat(auto-fit, minmax(120px, 1fr))",
                gap="6px", cell_styles=_hdr_cell,
            ) as g:
                for h in _headers:
                    with g.cell():
                        st_write(bs.table_hdr + s.center_txt, h)

            for name, pract, agile, tools, enterp, learn, is_active in _rows:
                cell = _active_cell if is_active else _normal_cell
                lbl = bs.table_lbl_active if is_active else bs.table_lbl
                with st_grid(
                    cols="repeat(auto-fit, minmax(120px, 1fr))",
                    gap="6px", cell_styles=cell,
                ) as g:
                    with g.cell():
                        st_write(lbl + s.center_txt, name)
                    for val in (pract, agile, tools, enterp, learn):
                        with g.cell():
                            st_write(bs.table_txt + s.center_txt, val)

    st_slide_break(marker_label="Enterprise Roadmap 2025-2030")

    # ── Slide 4: Enterprise Roadmap 2025-2030 ───────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "Enterprise Roadmap 2025-2030",
                tag=t.div, toc_lvl="+1",
                )
            st_hover_tooltip(
                title="Industry Analyst Predictions",
                entries=[
                    ("Convergence", "All major analysts agree: AI-assisted SE will become universal by 2028. The question is not IF but HOW."),
                    ("The failure mode", "Forrester predicts 50% of enterprises will try to replace developers with AI and fail — because they focus on tools, not process."),
                    ("The success mode", "Bain and McKinsey data shows 25-30% gains only with end-to-end process transformation, not tool adoption alone."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_zoom(120):
                with st_list(li_style=bs.body) as l:
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "Gartner "), (bs.body, "— "),
                                 (bs.stat, "90%"), (bs.body, " of enterprise SE will use AI by 2028"))
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "Bain "), (bs.body, "— "),
                                 (bs.stat, "25-30%"), (bs.body, " gains with process transformation"))
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "McKinsey "), (bs.body, "— Redesign processes around AI, don't bolt AI onto existing ones"))
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "Forrester "), (bs.body, "— "),
                                 (bs.stat, "50%"), (bs.body, " of enterprises will try to replace devs with AI — and fail"))

    st_slide_break(marker_label="Key Takeaways")

    # ── Slide 5: 3 Takeaways → GSE-One ─────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(
                bs.heading, "Key Takeaways",
                tag=t.div, toc_lvl="+1",
                )
            st_space("v", 1)
            with st_zoom(120):
                with st_list(li_style=bs.body) as l:
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "1. Process discipline persists "),
                                 (bs.body, "across all paradigms — structured always outperforms ad-hoc"))
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "2. The methodology is the multiplier "),
                                 (bs.body, "— tool alone "),
                                 (bs.stat, "~10%"),
                                 (bs.body, ", tool + process "),
                                 (bs.stat, "25-30%"))
                    with l.item():
                        st_write(bs.body,
                                 (bs.keyword, "3. The 80/20 rule "),
                                 (bs.body, "— planning and review = 80% of quality; execution = 20%"))

            st_space("v", 2)
            st_image(
                s.none, width="12%",
                uri="images/managed/GSE/images/logo-gse-geni-with-shield.webp",
            )
            st_write(bs.highlight, "Now let's experience GSE-One hands-on.")
