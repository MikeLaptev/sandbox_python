from random import uniform
from time import sleep


def target(name):
    while True:
        print(f"{name = }")
        sleep(uniform(0.1, 0.5))
        yield


def scheduler(*coros):
    while True:
        for coro in coros:
            next(coro)


if __name__ == "__main__":
    pool = {target(name=f"generator #{idx:02d}") for idx in range(3)}
    scheduler(*pool)
