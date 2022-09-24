# ttml-to-json

[![PyPI](https://img.shields.io/pypi/v/ttml-to-json.svg)](https://pypi.org/project/ttml-to-json/)
[![Changelog](https://img.shields.io/github/v/release/simonw/ttml-to-json?include_prereleases&label=changelog)](https://github.com/simonw/ttml-to-json/releases)
[![Tests](https://github.com/simonw/ttml-to-json/workflows/Test/badge.svg)](https://github.com/simonw/ttml-to-json/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/ttml-to-json/blob/master/LICENSE)

 Convert TTML to JSON

## Installation

Install this tool using `pip`:

    pip install ttml-to-json

## Usage

For help, run:

    ttml-to-json --help

You can also use:

    python -m ttml_to_json --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd ttml-to-json
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
