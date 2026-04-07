"""Slide — Category 4: Integrated Multi-Agent IDEs (Claude Code, Cursor, Copilot)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Integrated IDE styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    message = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_mai_message",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Category 4: Integrated Multi-Agent IDEs", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(300px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
        ) as g:
            # Claude Code
            with g.cell():
                st_write(bs.label, "Claude Code", tag=t.div)
                st_space("v", 0.5)
                st_write(
                    bs.body,
                    (bs.stat, "3 layers"), ": 5 sub-agents, Agent Teams with shared task lists, "
                    "Agent SDK for headless automation. ",
                    (bs.keyword, "17 hook event types"),
                    " for process enforcement.",
                )

            # Cursor
            with g.cell():
                st_write(bs.label, "Cursor", tag=t.div)
                st_space("v", 0.5)
                st_write(
                    bs.body,
                    "Up to ", (bs.stat, "8 parallel agents"),
                    " on isolated Git worktrees. "
                    "3 sub-agents (Explore, Bash, Browser). ",
                    (bs.keyword, "Background Agents"),
                    " on VMs for async tasks.",
                )

            # GitHub Copilot
            with g.cell():
                st_write(bs.label, "GitHub Copilot", tag=t.div)
                st_space("v", 0.5)
                st_write(
                    bs.body,
                    (bs.keyword, "Hybrid approach"),
                    ": Agent Mode (IDE, synchronous) + Coding Agent "
                    "(GitHub Actions, asynchronous). "
                    "Leverages ", (bs.stat, "widest distribution"),
                    " in the ecosystem.",
                )

        st_space("v", 2)
        st_write(bs.message, "Each occupies a unique strategic niche in the developer workflow.")
