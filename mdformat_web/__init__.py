from xml.etree import ElementTree

from bs4 import BeautifulSoup
import cssbeautifier
import jsbeautifier

__version__ = "0.2.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_js(unformatted: str, _info_str: str) -> str:
    return jsbeautifier.beautify(unformatted) + "\n"


def format_css(unformatted: str, _info_str: str) -> str:
    return cssbeautifier.beautify(unformatted) + "\n"


def format_html(unformatted: str, _info_str: str) -> str:
    # Use html.parser instead of lxml or html5lib to avoid adding an extra doctype.
    soup = BeautifulSoup(unformatted, features="html.parser")
    return soup.prettify()


def format_xml(unformatted: str, _info_str: str) -> str:
    element = ElementTree.fromstring(unformatted)
    ElementTree.indent(element)
    return ElementTree.tostring(element, encoding="unicode") + "\n"
