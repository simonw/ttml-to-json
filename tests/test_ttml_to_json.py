from click.testing import CliRunner
from ttml_to_json.cli import cli
import json
import pathlib
import pytest

test_path = pathlib.Path(__file__).parent / "demo.ttml"


EXPECTED = [
    {
        "start": "00:00:00.000",
        "end": "00:00:04.560",
        "lines": ["my career in side projects and open"],
    },
    {
        "start": "00:00:01.839",
        "end": "00:00:07.359",
        "lines": ["source basically this is so i've been"],
    },
    {
        "start": "00:00:04.560",
        "end": "00:00:08.880",
        "lines": ["knocking around with um uh side projects"],
    },
    {
        "start": "00:00:07.359",
        "end": "00:00:11.519",
        "lines": ["and open source things that"],
    },
    {
        "start": "00:00:08.880",
        "end": "00:00:12.719",
        "lines": ["20 years now it turns out and i realized"],
    },
    {"start": "00:00:11.519", "end": "00:00:14.880", "lines": ["recently that"]},
    {
        "start": "00:00:12.719",
        "end": "00:00:16.160",
        "lines": ["every key moment in my career started"],
    },
    {
        "start": "00:00:14.880",
        "end": "00:00:18.240",
        "lines": ["out as a side project"],
    },
]


def test_ttml_to_json():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, [str(test_path)])
        assert result.exit_code == 0
        assert json.loads(result.output) == EXPECTED


def test_ttml_to_json_output():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, [str(test_path), "-o", "output.json"])
        assert result.exit_code == 0
        assert json.load(open("output.json")) == EXPECTED


def test_ttml_to_json_output_single():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, [str(test_path), "-o", "output.json", "--single"])
        assert result.exit_code == 0
        actual = json.load(open("output.json"))
        assert actual == [
            {
                "start": "00:00:00.000",
                "end": "00:00:04.560",
                "line": "my career in side projects and open",
            },
            {
                "start": "00:00:01.839",
                "end": "00:00:07.359",
                "line": "source basically this is so i've been",
            },
            {
                "start": "00:00:04.560",
                "end": "00:00:08.880",
                "line": "knocking around with um uh side projects",
            },
            {
                "start": "00:00:07.359",
                "end": "00:00:11.519",
                "line": "and open source things that",
            },
            {
                "start": "00:00:08.880",
                "end": "00:00:12.719",
                "line": "20 years now it turns out and i realized",
            },
            {"start": "00:00:11.519", "end": "00:00:14.880", "line": "recently that"},
            {
                "start": "00:00:12.719",
                "end": "00:00:16.160",
                "line": "every key moment in my career started",
            },
            {
                "start": "00:00:14.880",
                "end": "00:00:18.240",
                "line": "out as a side project",
            },
        ]
