"""Slide — Phases 3-4: Work & Review details."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Work & Review slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    phase_title = s.bold + s.project.colors.primary + s.Large
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    analogy = s.project.titles.body + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Phases 3-4: Work & Review", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="24px",
            cell_styles=s.project.containers.cell_pad_md,
        ) as g:
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                    st_write(bs.phase_title, "Work", tag=t.div)
                    st_space("v", 0.5)
                    st_write(bs.body, (bs.keyword, "Three execution modes:"))
                    with st_list(li_style=bs.body, list_type=lt.ordered) as l:
                        with l.item():
                            st_write(bs.body, "Feature branch \u2014 standard isolation")
                        with l.item():
                            st_write(bs.body, (bs.keyword, "Worktree"), " \u2014 recommended, parallel work")
                        with l.item():
                            st_write(bs.body, "Direct on main \u2014 for small/solo projects")
                    st_space("v", 0.5)
                    with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, "Task tracking against the plan artifact")
                        with l.item():
                            st_write(bs.body, "Agent constrained to plan scope \u2014 no drift")

            with g.cell():
                with st_block(s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md):
                    st_write(bs.phase_title, "Review", tag=t.div)
                    st_space("v", 0.5)
                    st_write(bs.body, (bs.keyword, "Multi-perspective analysis:"))
                    with st_list(li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item():
                            st_write(bs.body, "Correctness \u2014 does it meet the plan?")
                        with l.item():
                            st_write(bs.body, "Security \u2014 vulnerability scanning")
                        with l.item():
                            st_write(bs.body, "Architecture \u2014 design consistency")
                        with l.item():
                            st_write(bs.body, "Learning extraction \u2014 what to compound")
                    st_space("v", 0.5)
                    st_write(bs.body, (bs.keyword, "Inputs: "), "PR, URL, branch, markdown, current branch")
                    st_space("v", 0.3)
                    st_write(bs.analogy, "Analogy: N-version verification \u2014 multiple perspectives catch different defects")
