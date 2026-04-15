"""GenSEM module styles — GSE methodology colors + shared base."""

from streamtex.styles import Style

from shared_styles import Styles as _SharedStyles


class GSEColors:
    """GSE methodology letter colors — used across all GenSEM blocks."""
    g = Style("color: #FFE06A;", "gse_g")   # G — Generative (jaune)
    s = Style("color: #64E6EE;", "gse_s")   # S — Software   (bleu)
    e = Style("color: #D3F4A2;", "gse_e")   # E — Engineering (vert)


class Styles(_SharedStyles):
    """GenSEM styles — inherits shared + adds GSE colors."""
    gse = GSEColors
