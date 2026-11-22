"""Slide — What we covered yesterday (day 1 recap)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Recap slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    question = Style.create(s.project.titles.body_accent + s.center_txt, "recap_question")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "What We Covered Yesterday", tag=t.div, toc_lvl="1", label="Welcome")
        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item(): st_write(bs.body, (bs.keyword, "GenAI basics"), " — what an LLM can and cannot do")
            with l.item(): st_write(bs.body, (bs.keyword, "VibeCoding"), " vs ", (bs.keyword, "VibeEngineering"))
            with l.item(): st_write(bs.body, (bs.keyword, "Tools"), " — opencode is our coding agent")
            with l.item(): st_write(bs.body, (bs.keyword, "Set-up"), " — your key, GSE-One, your ", (bs.keyword, "tutor window"), ", GitHub")
            with l.item(): st_write(bs.body, (bs.keyword, "FreeSelfApp"), " — a naive prototype, built fast")
        st_space("v", 1)
        st_write(bs.question, "Hands up: who would ship it to a customer?", tag=t.div)
