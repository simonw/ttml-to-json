import click
import json
from xml.etree import ElementTree as ET


@click.command()
@click.version_option()
@click.argument("path", type=click.File("r"))
@click.option(
    "-o",
    "--output",
    type=click.File("w"),
    default="-",
    help="File to write output to",
)
@click.option("-s", "--single", is_flag=True, help='Output single "line": per item')
def cli(path, output, single):
    "Convert TTML to JSON"
    et = ET.parse(path)
    els = et.findall(".//{http://www.w3.org/ns/ttml}div/{http://www.w3.org/ns/ttml}p")
    dicts = [
        {
            "start": el.attrib["begin"],
            "end": el.attrib["end"],
            "lines": [el.text],
        }
        for el in els
    ]
    if single:
        for d in dicts:
            d["line"] = "\n".join(d.pop("lines"))
    output.write(json.dumps(dicts, indent=2))
    output.write("\n")
    return
