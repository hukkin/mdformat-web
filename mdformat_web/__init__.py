import jsbeautifier
import cssbeautifier

__version__ = "0.0.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_js(unformatted: str, _info_str: str) -> str:
    return jsbeautifier.beautify(unformatted) + "\n"


def format_css(unformatted: str, _info_str: str) -> str:
    return cssbeautifier.beautify(unformatted) + "\n"
