# dependency inversion principles
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None: ...


class Email:
    def send(self, message: str) -> None:
        print(f"{self.__class__} - {message} has been sent")


class Notification:
    def notify(self, sender: Sender, message: str) -> None:
        print(f"{self.__class__} - notification about {message} has been sent")
        sender.send(message)


if __name__ == "__main__":
    m = "boom"
    e = Email()
    n = Notification()
    n.notify(e, m)
