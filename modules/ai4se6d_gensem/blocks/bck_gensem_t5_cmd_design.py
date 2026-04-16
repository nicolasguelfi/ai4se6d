"""Slide — /gse:design: architecture decisions and component decomposition."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.center_txt + s.text.wrap.hyphens, "t5cd_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "t5cd_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "t5cd_acc")
bs = BlockStyles


def build():
    st_marker("/gse:design")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "/gse:design \u2014 How Should It Work?", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="/gse:design \u2014 Architecture & Decisions",
                entries=[
                    ("Purpose", "Define architecture decisions, component decomposition, interface contracts, and technical choices. All significant choices are logged to the decision journal (DEC-)."),
                    ("Traces", "Design artefacts (DES-) trace to requirements (REQ-). Every design decision is justified by a DEC- entry."),
                    ("Agents invoked", "The architect agent evaluates structural quality and scalability. The security-auditor checks for attack surface."),
                    ("Output", "design.md with component diagram, interface contracts, and dependency map. Feeds /gse:preview and /gse:produce."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

        with st_zoom(90):
            _outputs = [
                ("\U0001f3d7\ufe0f", "Components", "Decomposition & responsibilities"),
                ("\U0001f517", "Interfaces", "Contracts between modules"),
                ("\U0001f4cb", "Decisions", "DEC- journal entries"),
                ("\U0001f5fa\ufe0f", "Dependencies", "External libs & services"),
            ]
            with st_grid(cols="1fr 1fr", gap="16px") as g:
                for i, (icon, label, desc) in enumerate(_outputs):
                    cell_style = _cell_acc if i % 2 == 0 else _cell
                    with g.cell():
                        with st_block(cell_style):
                            st_write(bs.body, f"{icon} ", (bs.keyword, label))
                            st_write(bs.body, desc)

            st_space("v", 1)
            st_write(bs.accent, "REQ \u2192 DES \u2192 DEC \u2014 every design choice is traceable and justified.")
