[![Build Status](https://github.com/hukkin/mdformat-web/actions/workflows/tests.yaml/badge.svg?branch=master)](<https://github.com/hukkin/mdformat-web/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![PyPI version](<https://img.shields.io/pypi/v/mdformat-web>)](<https://pypi.org/project/mdformat-web>)

# mdformat-web
> Mdformat plugin to format JS, CSS, HTML and XML code blocks

## Description
mdformat-web is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format JavaScript and CSS code blocks with [JS Beautifier](https://github.com/beautify-web/js-beautify),
HTML with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/),
and XML using the Python standard library.

## Installing
```bash
pip install mdformat-web
```

## Usage
```bash
mdformat YOUR_MARKDOWN_FILE.md
```
