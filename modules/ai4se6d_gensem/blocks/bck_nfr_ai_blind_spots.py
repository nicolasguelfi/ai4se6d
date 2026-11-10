"""Slide — What AI-generated code forgets: qualities nobody asked for (CCSET11, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """AI blind spots styles."""
    heading = s.project.titles.heading
    stat = s.project.titles.stat_hero_critical
    body = s.project.titles.body
    caption = Style.create(s.project.titles.body + s.center_txt, "blind_spots_caption")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(68):
            st_write(bs.heading, "What the Agent Forgets", tag=t.div, toc_lvl="+1", label="AI blind spots on qualities")
            st_write(bs.stat, "45%", tag=t.div)
            st_write(bs.caption, "of AI-generated code samples failed security tests.", tag=t.div)
            st_write(bs.source, cite("veracode-genai2025"), tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "Asked for qualities, a model proposes relevant ones — ",
                                        (s.project.citation, cite("lima-nfr-iso25010-2025")))
                with l.item(): st_write(bs.body, "Not asked, it optimises for \"it works on my screen\"")
