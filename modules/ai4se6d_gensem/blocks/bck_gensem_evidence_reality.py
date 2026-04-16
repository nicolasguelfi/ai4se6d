"""Slides — Perception gap, Developer surveys, 7h/week paradox, Daniotti 160K."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: evidence-insight
# @reuse: bck_gensem_evidence_perception, _surveys, _paradox_ai, _daniotti (v01)
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top

_hdr_cell = s.project.containers.table_header_cell
_normal_cell = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "real_body")
    accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.center_txt, "real_acc",
    )
    highlight = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt, "real_hl",
    )
    critical = Style.create(
        s.Large + s.bold + s.project.colors.critical + s.center_txt, "real_crit",
    )
    stat = Style.create(
        s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "real_stat",
    )
    stat_primary = Style.create(
        s.Huge + s.bold + s.project.colors.primary + s.center_txt, "real_stat_p",
    )
    source = s.project.citation + s.large + s.center_txt
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    table_lbl = s.project.titles.table_label
bs = BlockStyles


def build():
 
    st_slide_break(marker_label="Five Developer Surveys")

    # ── Slide: 5 Developer Surveys ──────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Five Developer Surveys", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Five Developer Surveys — What they tell us",
                        entries=[
                            ("What they are", "Five independent surveys (2025) collectively covering 95K+ developers worldwide, from different angles: usage, trust, productivity, and adoption."),
                            ("Key finding", "84-85% of developers now use AI tools daily, but trust in AI-generated code accuracy is declining (29% in 2025, down from 40%)."),
                            ("The paradox", "GitLab found teams lose 7h/week to AI-related inefficiencies — faster coding creates bottlenecks in review, debugging, and integration."),
                            ("Sources", "Stack Overflow 2025, JetBrains 2025, GitLab DevSecOps 2025, Pragmatic Engineer 2025, GitHub Octoverse 2025."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 1)

            with st_grid(
                cols="repeat(auto-fit, minmax(250px, 1fr))",
                gap="12px", cell_styles=_hdr_cell,
            ) as g:
                with g.cell():
                    st_write(bs.table_hdr + s.center_txt, "Survey")
                with g.cell():
                    st_write(bs.table_hdr + s.center_txt, "N")
                with g.cell():
                    st_write(bs.table_hdr + s.center_txt, "Key Finding")

            _surveys = [
                ("Stack Overflow 2025", "65K", "84% AI use, trust fell to 29%"),
                ("JetBrains 2025", "24.5K", "85% AI use, Cursor 17x YoY"),
                ("GitLab DevSecOps", "3.3K", "7h/week lost to AI inefficiencies"),
                ("Pragmatic Engineer", "2.6K", "Agents overtaking autocomplete"),
                ("GitHub Octoverse", "\u2014", "98% increase in new AI projects"),
            ]
            for survey, n, finding in _surveys:
                with st_grid(
                    cols="repeat(auto-fit, minmax(250px, 1fr))",
                    gap="12px", cell_styles=_normal_cell,
                ) as g:
                    with g.cell():
                        st_write(bs.table_lbl + s.center_txt, survey)
                    with g.cell():
                        st_write(bs.table_txt + s.center_txt, n)
                    with g.cell():
                        st_write(bs.table_txt + s.center_txt, finding)

    st_slide_break(marker_label="The AI Paradox")

    # ── Slide: 7h/week paradox ──────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "The AI Paradox", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The 7h/week Paradox — Explained",
                        entries=[
                            ("What they found", "GitLab surveyed 3,300 developers (2025). Teams using AI coding tools lose an average of 7 hours per team member per week to AI-related inefficiencies."),
                            ("How it happens", "AI generates code faster, but that code needs more review, creates more bugs to debug, and introduces integration problems — the downstream cost exceeds the upstream gain."),
                            ("Industry response", "85% of respondents now recognize platform engineering as essential to manage the complexity that AI-assisted development creates."),
                            ("GSE-One link", "The COMPOUND phase (/gse:compound) directly addresses this by capitalizing learnings so mistakes don't repeat."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.stat, "7h / week")
                st_space("v", 1)
                st_write(bs.body, "lost per team member to AI-related inefficiencies")
                st_space("v", 2)
                st_write(
                    bs.body,
                    "Faster coding creates bottlenecks elsewhere: review, debugging, integration.",
                )
                st_space("v", 1)
                st_write(bs.source, cite("gitlab-devsecops2025"))

    st_slide_break(marker_label="The 160,000-Developer Study")

    # ── Slide: Daniotti 160K ────────────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "The 160,000-Developer Study", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="The 160K Study — Explained",
                        entries=[
                            ("What they did", "Daniotti et al. analyzed the coding activity of 160,000+ developers on GitHub to measure how AI tools affect productivity across experience levels."),
                            ("What they found", "Experienced senior developers captured nearly ALL measurable productivity gains. Early-career developers showed NO significant benefits."),
                            ("Why it contradicts Cui", "In Cui's enterprise study, juniors gained +27-39% because they received structured support and mentoring. On open-source (no support), AI rewards existing expertise."),
                            ("Key takeaway", "Without a structured methodology, only developers who already know what they're doing benefit from AI — everyone else gets lost."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            with st_zoom(120):
                st_space("v", 2)
                st_write(bs.stat_primary, "160K+")
                st_space("v", 1)
                st_write(bs.body, "GitHub developers analyzed by Daniotti et al.")
                st_space("v", 1)
                st_write(
                    bs.accent,
                    "Seniors capture ALL gains. Juniors show NO significant benefits.",
                )
                st_space("v", 1)
                st_write(bs.source, cite("daniotti-github2025"))
