from typing import Protocol


class Obstacle(Protocol):
    def action(self) -> str: ...


class Hero(Protocol):
    def interact_with(self, obstacle: Obstacle) -> None: ...


class GameFactory(Protocol):
    def make_character(self) -> Hero: ...

    def make_obstacle(self) -> Obstacle: ...


class Frog:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: Obstacle) -> None:
        act: str = obstacle.action()
        msg: str = f"{self} the Frog encounters {obstacle} and {act}"
        print(msg)


class Bug:

    def __str__(self) -> str:
        return "a bug"

    def action(self) -> str:
        return "eats it"


class FrogWorld:

    def __init__(self, player_name: str) -> None:
        print(self)
        self.player_name = player_name

    def __str__(self) -> str:
        return "\n\n\t------ Frog World ------"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class GameEnvironment:
    def __init__(self, factory: GameFactory) -> None:
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


if __name__ == "__main__":
    name: str = input("enter name: ")
    game: GameFactory = FrogWorld
    environment = GameEnvironment(game(name))
    environment.play()
