import json
from pathlib import Path
from typing import Union
from xml.etree import ElementTree


class JSONDataExtractor:

    def __init__(self, path: Path) -> None:
        self.data = {}
        with open(path, "r") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:

    def __init__(self, path: Path) -> None:
        self.tree = ElementTree.parse(path)

    @property
    def parsed_data(self):
        return self.tree


def extract_data(path: Path) -> Union[JSONDataExtractor, XMLDataExtractor]:
    extension: str = path.name.split(".")[-1]
    if extension == "json":
        return JSONDataExtractor(path)
    elif extension == "xml":
        return XMLDataExtractor(path)

    raise ValueError("Unsupported file")


if __name__ == "__main__":
    dir_path: Path = Path(__file__).parent
    files = ["movies.json", "person.xml"]
    for f in files:
        print(extract_data(path=(dir_path / Path(f))).parsed_data)
