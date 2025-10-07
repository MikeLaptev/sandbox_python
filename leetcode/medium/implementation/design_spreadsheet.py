from typing import Dict


class DesignSpreadsheet:

    def __init__(self, rows: int):
        self.cells: Dict[str, int] = {}

    def set_cell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def reset_cell(self, cell: str) -> None:
        self.cells[cell] = 0

    def get_value(self, formula: str) -> int:
        p1, p2 = formula[1:].split("+")
        r: int = 0
        if p1.isdigit():
            r += int(p1)
        else:
            r += self.cells.get(p1, 0)

        if p2.isdigit():
            r += int(p2)
        else:
            r += self.cells.get(p2, 0)

        return r


if __name__ == "__main__":
    spreadsheet = DesignSpreadsheet(3)
    assert 12 == spreadsheet.get_value("=5+7")
    spreadsheet.set_cell("A1", 10)
    assert 16 == spreadsheet.get_value("=A1+6")
    spreadsheet.set_cell("B2", 15)
    assert 25 == spreadsheet.get_value("=A1+B2")
    spreadsheet.reset_cell("A1")
    assert 15 == spreadsheet.get_value("=A1+B2")
