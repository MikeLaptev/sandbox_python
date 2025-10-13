# liskov substitution principle


class BirdV:
    def fly(self) -> None:
        print("I can fly")


class PenguinV(BirdV):
    def fly(self) -> None:
        print("I can't fly")


def make_birdv_fly(*birds: BirdV) -> None:
    for bird in birds:
        bird.fly()


class Bird:
    def move(self) -> None:
        print("I can move")


class FlyingBird(Bird):
    def move(self) -> None:
        print("I can fly")


class FlightlessBird(Bird):
    def move(self) -> None:
        print("I can't fly")


def make_bird_move(*birds: Bird) -> None:
    for bird in birds:
        bird.move()


if __name__ == "__main__":
    # violation
    bv = BirdV()
    pv = PenguinV()
    make_birdv_fly(bv, pv)

    # lsp
    b = Bird()
    e = FlyingBird()
    p = FlightlessBird()
    make_bird_move(b, e, p)
