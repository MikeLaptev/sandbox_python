# interface segregation principle
from typing import Protocol


class Printer(Protocol):
    def print_document(self) -> None: ...


class Scanner(Protocol):
    def scan_document(self) -> None: ...


class Copier(Protocol):
    def copy_document(self) -> None: ...


class AllInOnePrinter:

    def print_document(self) -> None:
        print(f"{self.__class__} - printing...")

    def scan_document(self) -> None:
        print(f"{self.__class__} - scanning...")

    def copy_document(self) -> None:
        print(f"{self.__class__} - copying...")


class SimplePrinter:
    def print_document(self):
        print(f"{self.__class__} - printing...")


def print_me(*printers: Printer):
    for printer in printers:
        printer.print_document()


if __name__ == "__main__":
    p = SimplePrinter()
    a = AllInOnePrinter()
    print_me(a, p)
