# open-closed principle
import math
from typing import Protocol, List


class Shape(Protocol):
    def area(self) -> float:
        pass


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius


def area_calculator(*shapes: Shape) -> List[float]:
    return [shape.area() for shape in shapes]


if __name__ == "__main__":
    p: float = 5.0
    r: Rectangle = Rectangle(p, p)
    c: Circle = Circle(p)
    print(*[f"{v:.2f}" for v in area_calculator(r, c)])
