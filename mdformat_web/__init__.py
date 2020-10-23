from bs4 import BeautifulSoup
import cssbeautifier
import jsbeautifier

__version__ = "0.1.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_js(unformatted: str, _info_str: str) -> str:
    return jsbeautifier.beautify(unformatted) + "\n"


def format_css(unformatted: str, _info_str: str) -> str:
    return cssbeautifier.beautify(unformatted) + "\n"


def format_html(unformatted: str, _info_str: str) -> str:
    soup = BeautifulSoup(unformatted, features="lxml")
    return soup.prettify() + "\n"


def format_xml(unformatted: str, _info_str: str) -> str:
    soup = BeautifulSoup(unformatted, features="lxml-xml")
    return soup.prettify() + "\n"
