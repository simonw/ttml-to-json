from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="ttml-to-json",
    description=" Convert TTML to JSON",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/ttml-to-json",
    project_urls={
        "Issues": "https://github.com/simonw/ttml-to-json/issues",
        "CI": "https://github.com/simonw/ttml-to-json/actions",
        "Changelog": "https://github.com/simonw/ttml-to-json/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["ttml_to_json"],
    entry_points="""
        [console_scripts]
        ttml-to-json=ttml_to_json.cli:cli
    """,
    install_requires=["click"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
