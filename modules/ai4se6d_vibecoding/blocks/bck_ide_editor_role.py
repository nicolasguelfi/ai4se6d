"""Act IV — Where an IDE fits in this course: the editor reads, opencode writes (NG, 2026-11-22)."""
# Source: ai4se-kit/syllabus/ide-guide.md (kit 2026-11-22.3)
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """IDE role slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    lead = Style.create(s.project.titles.body + s.center_txt, "ide_editor_role_lead")
    column_title = Style.create(s.project.titles.subtitle + s.center_txt, "ide_editor_role_column_title")
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    keyword_critical = s.bold + s.project.colors.critical
    takeaway = Style.create(
        s.large + s.italic + s.project.colors.accent + s.center_txt,
        "ide_editor_role_takeaway",
    )
bs = BlockStyles

_LEAD_ZOOM = 75
_GRID_ZOOM = 50  # eight bullets in two columns: scaled to fit one screen like the neighbouring slides


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Where an IDE Fits in This Course", tag=t.div, toc_lvl="1")
            with st_zoom(_LEAD_ZOOM):
                st_write(
                    bs.lead,
                    (bs.keyword, "opencode"), " changes the project. The editor is for ",
                    (bs.keyword_accent, "reading"), " it. No step requires an editor.",
                    tag=t.div,
                )

            with st_zoom(_GRID_ZOOM), st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.callout,
            ) as g:
                with g.cell():
                    st_write(bs.column_title, "Four uses", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_accent, "Read the code"), " — the whole tree at a glance")
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_accent, "See what the agent changed"),
                                " — Source Control, green/red diff",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_accent, "Read the Markdown"),
                                " — plans, reqs, reviews (preview)",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_accent, "Fix one line by hand"),
                                " — save, then tell opencode",
                            )
                with g.cell():
                    st_write(bs.column_title, "Workshops: the editor's AI stays off", tag=t.div)
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, (bs.keyword_critical, "Two agents"), " overwrite each other")
                        with l.item():
                            st_write(bs.body, (bs.keyword_warn, "The editor's agent"), " also reads AGENTS.md")
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_warn, "Completion"),
                                " writes your test for you (day 2)",
                            )
                        with l.item():
                            st_write(
                                bs.body, (bs.keyword_critical, "Agent extensions"),
                                " (Cline, Continue, Kilo) bring a second agent back",
                            )

            st_write(
                bs.takeaway,
                "Commits, branches and merges stay with opencode and GSE-One: "
                "no Commit or Sync button in the editor.",
                tag=t.div,
            )
