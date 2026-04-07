"""Slide — Orchestration commands: /lfg and /slfg."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """LFG orchestration slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    cmd = s.bold + s.project.colors.highlight
bs = BlockStyles

def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Orchestration: /lfg and /slfg", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="32px",
        ) as g:
            with g.cell():
                st_write(bs.cmd, "/lfg \u2014 Sequential Chain", tag=t.div)
                st_space("v", 1)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                    with l.item():
                        st_write(bs.body, "Plan the feature")
                    with l.item():
                        st_write(bs.body, "Work (implement in worktree)")
                    with l.item():
                        st_write(bs.body, "Review (multi-perspective)")
                    with l.item():
                        st_write(bs.body, "Run tests to verify")
                    with l.item():
                        st_write(bs.body, "DONE \u2014 merge to main")
                st_space("v", 1)
                st_write(bs.body, (bs.keyword, "Best for: "), "Profile B developers \u2014 one feature at a time, full visibility.")

            with g.cell():
                st_write(bs.cmd, "/slfg \u2014 Parallel Execution", tag=t.div)
                st_space("v", 1)
                with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                    with l.item():
                        st_write(bs.body, "Multiple worktrees in parallel")
                    with l.item():
                        st_write(bs.body, "Each feature gets its own plan/work/review cycle")
                    with l.item():
                        st_write(bs.body, "Automated conflict detection across worktrees")
                    with l.item():
                        st_write(bs.body, "Merge queue with dependency ordering")
                st_space("v", 1)
                st_write(bs.body, (bs.keyword, "Best for: "), "Profile C developers \u2014 maximum throughput, orchestrating multiple AI agents.")

        st_space("v", 1)
        st_write(bs.body, (bs.label, "Learning tip: "), "Start with individual phases to understand each step, then graduate to /lfg, then /slfg.")
