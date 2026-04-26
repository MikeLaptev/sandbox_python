from random import uniform
from time import perf_counter
from collections import namedtuple

Sleep = namedtuple("Sleep", "sleep_time")


def target(name):
    while True:
        print(f"{name = }")
        yield Sleep(uniform(0.1, 0.5))


def scheduler(*coros):
    coros = {coro: None for coro in coros}
    while True:
        for coro in coros:
            if coros[coro] is not None and perf_counter() < coros[coro]:

                continue
            print("time to run")
            coros[coro] = None
            res = next(coro)
            if isinstance(res, Sleep):
                coros[coro] = res.sleep_time + perf_counter()
                print(f"{coros[coro] = }")


if __name__ == "__main__":
    pool = {target(name=f"generator #{idx:02d}") for idx in range(3)}
    scheduler(*pool)
