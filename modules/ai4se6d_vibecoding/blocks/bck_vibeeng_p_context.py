"""Slide — P6: Context Engineering (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """P6 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p6_number",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A central hub circle in amber surrounded by orbiting information "
    "spheres in electric blue and teal — documents, rules, tools. Lines connect "
    f"everything. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "P6 — Context Engineering", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p6_context",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    st_write(bs.number, "6")
                    st_space("v", 1)
                    with st_zoom(90):
                        st_write(
                            bs.body,
                            (bs.keyword, "Systematically managing"),
                            " the information fed to AI agents.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            "Not clever prompting \u2014 structured ",
                            (bs.keyword, "project rules"),
                            ", ",
                            (bs.keyword, "memory"),
                            ", and ",
                            (bs.keyword, "tool configurations"),
                            ".",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (bs.accent, "Project rules"),
                            ", ",
                            (bs.accent, "MCP servers"),
                            ", ",
                            (bs.accent, "memory systems"),
                            " \u2014 the agent sees what you curate.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "Your pantry, your prep, your standards "
                            "\u2014 maintained every day, not just on opening night."),
                        )
