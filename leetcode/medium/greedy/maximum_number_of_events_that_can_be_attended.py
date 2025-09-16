import heapq
from queue import PriorityQueue
from typing import List


class MaximumNumberOfEventsThatCanBeAttended:
    """
    Leetcode #1353
    Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended
    """

    def max_events(self, events: List[List[int]]) -> int:
        """
        >>> sut = MaximumNumberOfEventsThatCanBeAttended()
        >>> events = [[1, 2], [2, 3], [3, 4], [1, 2]]
        >>> actual = sut.max_events(events)
        >>> assert 4 == actual, f"expected 4, got {actual}"
        >>> events = [[1, 2], [2, 3], [3, 4]]
        >>> actual = sut.max_events(events)
        >>> assert 3 == actual, f"expected 3, got {actual}"
        """
        # events are sorted by the start time
        events.sort(key=lambda x: x[0])
        last_day = max([x[1] for x in events])

        # from all the events which can be participated during a day,
        # choosing the one that's start earlier
        pq = PriorityQueue()
        j = 0
        result = 0
        for i in range(0, last_day + 1):
            while j < len(events) and events[j][0] <= i:
                pq.put(events[j][1])
                j += 1
            while not pq.empty():
                t = pq.get()
                if t >= i:
                    pq.put(t)
                    break
            if not pq.empty():
                pq.get()
                result += 1

        return result

    def max_events_opt(self, events: List[List[int]]) -> int:
        """
        >>> sut = MaximumNumberOfEventsThatCanBeAttended()
        >>> events = [[1, 2], [2, 3], [3, 4], [1, 2]]
        >>> actual = sut.max_events_opt(events)
        >>> assert 4 == actual, f"expected 4, got {actual}"
        >>> events = [[1, 2], [2, 3], [3, 4]]
        >>> actual = sut.max_events_opt(events)
        >>> assert 3 == actual, f"expected 3, got {actual}"
        """
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
