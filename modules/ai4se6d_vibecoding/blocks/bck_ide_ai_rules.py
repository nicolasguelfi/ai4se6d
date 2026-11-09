"""Act IV — Practical rules for this week: what never goes into a prompt, what to allow the agent."""
# Adapted from streamtex-all-trainings@7707c1c5:content/atoms/bck_llm_pe_rester_responsable.py
# Adapted from streamtex-all-trainings@7707c1c5:content/illustrations/prompt_engineering/bck_pei_donnees_sensibles_a.py
# Adapted from streamtex-all-trainings@7707c1c5:content/genai_landscape/bck_genai_on_computer_concept.py
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Practical rules slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    column_title = Style.create(
        s.project.titles.subtitle + s.center_txt,
        "ide_ai_rules_column_title",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    keyword_critical = s.bold + s.project.colors.critical
    takeaway = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_ai_rules_takeaway",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Rules for This Week", tag=t.div, toc_lvl="2")

            with st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.callout,
            ) as g:
                with g.cell():
                    st_write(bs.column_title, "Never in a prompt", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_critical, "Secrets"), " — keys (yours too), passwords, .env")
                        with l.item():
                            st_write(bs.body, (bs.keyword_critical, "Personal data"), " — names, e-mails, health")
                        with l.item():
                            st_write(bs.body, (bs.keyword_critical, "NDA code"), " — anonymise first")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "Remember"), " — a prompt leaves your machine")
                with g.cell():
                    st_write(bs.column_title, "What the agent may do", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "One project folder"), " — never your home")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Ask before"), " any shell command")
                        with l.item():
                            st_write(bs.body, (bs.keyword_critical, "Never --bypass"), " on a real machine")
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Review every diff"), " before commit")

            st_write(
                bs.takeaway,
                "The AI proposes. You answer for what goes out.",
                tag=t.div,
            )
