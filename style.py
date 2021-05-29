from pygments.style import Style
from pygments.token import Text


class ThesisStyle(Style):
    default_style = ""

    styles = {
        Text: "#663333",
    }
