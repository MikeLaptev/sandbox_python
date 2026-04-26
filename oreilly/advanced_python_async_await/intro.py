from contextlib import contextmanager
from time import perf_counter
import numpy as np


@contextmanager
def timed():
    try:
        before = perf_counter()
        yield
    finally:
        after = perf_counter()
    print(f"\N{MATHEMATICAL BOLD CAPITAL DELTA}t: {after - before:4}s")


rng = np.random.default_rng(0)


if __name__ == "__main__":
    with timed():
        xs = rng.random(size=(100, 100))
        np.linalg.inv(xs)

    with timed():
        xs = rng.random(size=(500, 500))
        np.linalg.inv(xs)

    with timed():
        xs = rng.random(size=(2500, 2500))
        np.linalg.inv(xs)
