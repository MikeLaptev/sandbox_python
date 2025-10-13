class Engine:
    def start(self):
        print("engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("car started")


if __name__ == "__main__":
    my_car = Car()
    my_car.start()
