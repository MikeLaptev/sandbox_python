from abc import ABC, abstractmethod
from typing import List


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"{self.__class__}: {message}")


class ConsoleUppercaseLogger(Logger):
    def log(self, message: str) -> None:
        print(f"{self.__class__}: {message.upper()}")


def info(logger: Logger, message: str) -> None:
    logger.log(f"info: {message}")


class Application:

    def __init__(self, loggers: List[Logger]) -> None:
        self.loggers = loggers

    def action(self):
        print("action ... ")
        for l in self.loggers:
            l.log("action applied")


if __name__ == "__main__":
    c = ConsoleLogger()
    info(c, "simple message")
    cu = ConsoleUppercaseLogger()
    info(cu, "simple message")

    a = Application([c, cu])
    a.action()
