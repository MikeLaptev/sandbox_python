from typing import Protocol


class Logger(Protocol):

    def log(self, message: str) -> None: ...


class ConsoleLogger:
    def log(self, message: str) -> None:
        print(message)


class ConsoleUppercaseLogger:
    def log(self, message: str) -> None:
        print(message.upper())


def warn(logger: Logger, message: str) -> None:
    logger.log(f"warn: {message}")


if __name__ == "__main__":
    c = ConsoleLogger()
    warn(c, "simple message")
    cu = ConsoleUppercaseLogger()
    warn(cu, "simple message")
