"""Styles for the AI4SE 6D collection."""

from streamtex.styles import StxStyles, Style, Text


class Styles(StxStyles):
    """AI4SE 6D collection styles."""

    class project:
        class colors:
            accent_blue = Style("color: #7AB8F5;", "ai4se6d_accent_blue")
            highlight_purple = Style("color: #764ba2;", "ai4se6d_highlight_purple")

        class titles:
            main_title = Style.create(
                StxStyles.Huge + Text.weights.bold_weight,
                "ai4se6d_main_title",
            )
            section_title = Style.create(
                Style("color: #7AB8F5;", "_at") + Text.weights.bold_weight + Text.sizes.LARGE_size,
                "ai4se6d_section_title",
            )
