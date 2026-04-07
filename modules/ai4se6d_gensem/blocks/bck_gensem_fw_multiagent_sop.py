"""Slide — Category 1: SOP-Driven Pipelines (MetaGPT, ChatDev, FlowGen, AgentCoder)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """SOP-driven pipelines styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    callout_body = s.project.titles.body
    source = s.project.titles.source
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Category 1: SOP-Driven Pipelines", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "MetaGPT"), " (ICLR 2024 Oral, ", (bs.stat, "51K\u2605"), "): "
                    "5 roles (PM, architect, project manager, engineer, QA). "
                    "SOPs encoded into prompt sequences. ",
                    (bs.keyword, "Structured artifacts"), ", NOT free-form chat.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "ChatDev"), " (ACL 2024, ", (bs.stat, "26K\u2605"), "): "
                    "Chat chains across design/coding/testing phases. ",
                    (bs.keyword, "Communicative dehallucination"),
                    " via cross-agent dialogue.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "FlowGen"), ": Emulates Waterfall/TDD/Scrum with LLM agents. ",
                    (bs.stat, "15% Pass@1 improvement"), " over unstructured baselines.",
                )
            with l.item():
                st_write(
                    bs.body,
                    (bs.label, "AgentCoder"), ": 3-agent system (programmer, test designer, executor). ",
                    (bs.stat, "96.3% pass@1"), " on HumanEval.",
                )

        st_space("v", 2)
        # Key finding callout
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_body,
                (bs.stat, "Key finding: "),
                "Encoding workflow discipline into agents ",
                (bs.keyword, "improves output quality"),
                " compared to unconstrained generation.",
            )

        st_space("v", 1)
        st_write(
            bs.source,
            cite("hong-metagpt2024"), " | ",
            cite("qian-chatdev2024"), " | ",
            cite("soen101-2024"), " | ",
            cite("huang-agentcoder2024"),
        )
