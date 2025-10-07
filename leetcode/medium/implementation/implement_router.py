import bisect
from typing import List, Dict, Tuple, Set


class Router:

    def __init__(self, memory_limit: int) -> None:
        self.memory_limit = memory_limit
        self.counter = 0

        # dict of destination to dict of source to time
        self.packets: Set[Tuple[int, int, int]] = set()
        # dict of destination to time, based on the description, list will be sorted
        self.destinations: Dict[int, List[int]] = {}
        self.packets_queue: List[Tuple[int, int, int]] = []

    def add_packet(self, source: int, destination: int, timestamp: int) -> bool:
        """
        Note: that queries for add_packet will be made in non-decreasing order of timestamp.
        """
        if (source, destination, timestamp) in self.packets:
            return False

        self.counter += 1

        self.packets.add((source, destination, timestamp))

        if not destination in self.destinations:
            self.destinations[destination] = []
        self.destinations[destination].append(timestamp)
        self.packets_queue.append((source, destination, timestamp))

        while self.counter > self.memory_limit:
            self.forward_packet()

        return True

    def forward_packet(self) -> List[int]:
        if not self.packets_queue:
            return []

        f = self.packets_queue.pop(0)

        # clean packets
        self.packets.remove(f)

        # clean destinations
        self.destinations[f[1]].pop(0)
        if not self.destinations[f[1]]:
            del self.destinations[f[1]]

        self.counter -= 1
        return list(f)

    def get_count(self, destination: int, start_time: int, end_time: int) -> int:
        if not destination in self.destinations:
            return 0
        l: int = bisect.bisect_left(self.destinations[destination], start_time)
        r: int = bisect.bisect_right(self.destinations[destination], end_time, lo=l)

        return r - l


if __name__ == "__main__":
    # use-case 1
    router = Router(3)
    assert True == router.add_packet(1, 4, 1)
    assert True == router.add_packet(3, 1, 1)
    assert True == router.add_packet(3, 1, 3)
    p = router.forward_packet()
    assert [1, 4, 1] == p, f"expected [1, 4, 1]; got {p}"
    assert True == router.add_packet(3, 5, 3)
    assert True == router.add_packet(5, 2, 7)
    assert True == router.add_packet(2, 4, 7)

    # use-case 2
    router = Router(2)
    assert True == router.add_packet(4, 3, 1)
    assert True == router.add_packet(5, 1, 1)
    assert True == router.add_packet(3, 2, 1)
    assert False == router.add_packet(5, 1, 1)
    assert True == router.add_packet(4, 2, 1)
    assert True == router.add_packet(5, 3, 1)
    p = router.forward_packet()
    assert [4, 2, 1] == p, f"expected [4, 2, 1]; got {p}"

    # use-case 3
    router = Router(2)
    assert True == router.add_packet(2, 1, 3145728)
    assert True == router.add_packet(2, 3, 3145728)
    assert [2, 1, 3145728] == router.forward_packet()
    assert [2, 3, 3145728] == router.forward_packet()

    # use-case 4
    router = Router(3)
    assert True == router.add_packet(1, 4, 90)
    assert True == router.add_packet(2, 5, 90)
    assert False == router.add_packet(1, 4, 90)
    assert True == router.add_packet(3, 5, 95)
    assert True == router.add_packet(4, 5, 105)
    assert [2, 5, 90] == router.forward_packet()
    assert True == router.add_packet(5, 2, 110)
    c = router.get_count(5, 100, 110)
    assert 1 == c, f"expected 1, got {c}"

    # use-case 5
    router = Router(2)
    assert True == router.add_packet(7, 4, 90)
    assert [7, 4, 90] == router.forward_packet()
    assert [] == router.forward_packet()
