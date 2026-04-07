"""Slide — Category 2: Conversational Collaboration (AutoGen, CAMEL/OWL, CrewAI)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Conversational collaboration styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    message = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_mac_message",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Category 2: Conversational Collaboration", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(300px, 1fr))",
            gap="16px",
            cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md,
        ) as g:
            with g.cell():
                st_write(bs.label, "AutoGen / AG2", tag=t.div)
                st_write(bs.body, "Microsoft, ", (bs.stat, "40K\u2605"))
                st_space("v", 0.5)
                st_write(
                    bs.body,
                    (bs.keyword, "Customizable conversable agents"),
                    ". Foundational infrastructure for multi-agent systems. "
                    "Flexible topology \u2014 agents negotiate roles at runtime.",
                )

            with g.cell():
                st_write(bs.label, "CAMEL / OWL", tag=t.div)
                st_write(bs.body, "NeurIPS 2023")
                st_space("v", 0.5)
                st_write(
                    bs.body,
                    (bs.keyword, "Role-playing with inception prompting"),
                    ". Research-oriented framework transitioning to production. "
                    "Agents assume personas to explore solution spaces.",
                )

            with g.cell():
                st_write(bs.label, "CrewAI", tag=t.div)
                st_write(bs.body, (bs.stat, "44K\u2605"))
                st_space("v", 0.5)
                st_write(
                    bs.body,
                    (bs.keyword, "Industry-oriented"),
                    ". High-level abstractions for roles, goals, and backstories. "
                    "Lowest barrier to entry for team-based agent orchestration.",
                )

        st_space("v", 2)
        st_write(
            bs.message,
            "Characteristic: flexible multi-turn dialogue, less structured than SOP-driven.",
        )
