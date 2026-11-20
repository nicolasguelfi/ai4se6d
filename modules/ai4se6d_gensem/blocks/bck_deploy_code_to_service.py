"""Slide — From code to a service: build, image, container, address (CCSET16, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Code-to-service styles."""
    heading = s.project.titles.heading
    step = Style.create(s.project.titles.table_label + s.center_txt, "code_service_step")
    what = Style.create(s.project.titles.table_cell + s.center_txt, "code_service_what")
    body = s.project.titles.body
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

STEPS = [
    ("Code", "your repository, at a tag"),
    ("Build", "install, test, compile"),
    ("Image", "all it needs to run, frozen"),
    ("Container", "the image, running on a server"),
    ("Address", "a name and HTTPS"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(66):
            st_write(bs.heading, "From Code to a Service", tag=t.div, toc_lvl="+1", label="From code to a service")
            with st_grid(cols="repeat(5, 1fr)", gap="10px", cell_styles=s.project.containers.table_normal_cell) as g:
                for i, (step, what) in enumerate(STEPS):
                    with g.cell():
                        st_write(bs.step, step + ("  →" if i < len(STEPS) - 1 else ""), tag=t.div)
                        st_write(bs.what, what, tag=t.div)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.body, "\"It works on my machine\" is not a service: another machine, other "
                                        "versions, and nobody there to restart it")
                with l.item(): st_write(bs.body, "Build once, deploy the same image everywhere: what you tested is what runs")
                with l.item(): st_write(bs.body, "Every step is a script, not a memory: the same result each time")
            st_write(bs.source, cite("humble-farley-cd2010"), tag=t.div)
