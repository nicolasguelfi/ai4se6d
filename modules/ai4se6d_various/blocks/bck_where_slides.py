from streamtex import *  # noqa: F403
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    title = s.project.titles.slide_title + s.center_txt
    content = s.project.titles.body
    link = s.project.titles.body + s.bold + s.project.colors.primary


bs = BlockStyles

_COURSEPACK_URL = (
    "https://docs.google.com/document/d/"
    "1QbFuAHncO54t-o3Gu6SKudhO-ADz6TD_5EVXYYPJyRk/edit?tab=t.0"
)
_CONCEPTS_URL = "https://ai4se6d.streamtex.org"
_PRACTICALS_URL = (
    "https://drive.google.com/drive/folders/"
    "1-eQIoGfSxmMwPEHsdK50ynPfmN38bC7y?usp=sharing"
)


def build():
    st_write(bs.title, "Q/A: Where Are All the Slides?", tag=t.div, toc_lvl="1")
    st_space(size=2)

    with st_list(list_type=lt.unordered, li_style=bs.content) as li:
        with li.item():
            st_write(
                (bs.link, "COURSEPACK", _COURSEPACK_URL),
                (bs.content, " — Course reference document"),
            )
        with li.item():
            st_write(
                (bs.link, "CONCEPTS", _CONCEPTS_URL),
                (bs.content, " — Key concepts and reference diagrams"),
            )
        with li.item():
            st_write(
                (bs.link, "PRACTICALS", _PRACTICALS_URL),
                (bs.content, " — Hands-on exercises and lab materials"),
            )
