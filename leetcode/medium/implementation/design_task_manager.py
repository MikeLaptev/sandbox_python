from dataclasses import dataclass, field
from heapq import heappush, heapify, heappop
from typing import List, Dict, Tuple


class TaskManager:
    """
    Leetcode #3408
    Link: https://leetcode.com/problems/design-task-manager
    """

    def __init__(self, tasks: List[List[int]]) -> None:
        self.__pq: List[Tuple[int, int, int]] = []
        self.__by_task_id: Dict[int, Tuple[int, int, int]] = dict()
        for task in tasks:
            self.add(*task)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        t = (-priority, -task_id, user_id)
        self.__by_task_id[-task_id] = t
        heappush(self.__pq, t)

    def edit(self, task_id: int, new_priority: int) -> None:
        _, _, user_id = self.__by_task_id[-task_id]
        t = (-new_priority, -task_id, user_id)
        self.__by_task_id[-task_id] = t
        heappush(self.__pq, t)

    def rmv(self, task_id: int) -> None:
        del self.__by_task_id[-task_id]

    def exec_top(self) -> int:
        while self.__pq:
            task = heappop(self.__pq)
            _, task_id, user_id = task

            if self.__by_task_id.get(task_id) is not task:
                continue

            del self.__by_task_id[task_id]
            return user_id

        return -1


class TaskManagerNonOpt:
    """
    Leetcode #3408
    Link: https://leetcode.com/problems/design-task-manager
    """

    def __init__(self, tasks: List[List[int]]):
        self.__pq: List[Task] = []
        self.__by_task_id: Dict[int, Task] = dict()
        for task in tasks:
            self.add(*task)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        # making both priority and task_id negatives to maintain invariant of max heap
        t: Task = Task(-priority, -task_id, user_id, False)
        self.__pq.append(t)
        self.__by_task_id[task_id] = t

    def edit(self, task_id: int, new_priority: int) -> None:
        t: Task = self.__by_task_id[task_id]
        t.priority = -new_priority

    def rmv(self, task_id: int) -> None:
        t: Task = self.__by_task_id[task_id]
        t.removed = True
        self.__pq.remove(t)

    def exec_top(self) -> int:
        heapify(self.__pq)
        while self.__pq:
            t: Task = heappop(self.__pq)
            if not t.removed:
                return t.user_id
        return -1


@dataclass(order=True)
class Task:
    priority: int
    task_id: int
    user_id: int = field(compare=False)
    removed: bool = field(compare=False)


if __name__ == "__main__":
    # case 1.1:
    sut = TaskManagerNonOpt([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    sut.add(4, 104, 5)
    sut.edit(102, 8)
    assert 3 == sut.exec_top()
    sut.rmv(101)
    sut.add(5, 105, 15)
    assert 5 == sut.exec_top()
    assert 2 == sut.exec_top()

    # case 1.2:
    sut = TaskManagerNonOpt([[10, 26, 25]])
    sut.rmv(26)
    assert -1 == sut.exec_top()

    # case 1.3:
    sut = TaskManagerNonOpt([[6, 4, 48], [2, 7, 45], [6, 28, 44], [10, 27, 10]])
    assert 6 == sut.exec_top()
    sut.rmv(7)
    assert 6 == sut.exec_top()

    # case 1.4
    sut = TaskManagerNonOpt([[1, 1, 1]])
    sut.add(4, 104, 5)
    sut.rmv(104)
    sut.add(4, 104, 5)
    assert 4 == sut.exec_top()
    sut.add(5, 105, 2)
    assert 5 == sut.exec_top()

    # case 2.1:
    sut = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    sut.add(4, 104, 5)
    sut.edit(102, 8)
    assert 3 == sut.exec_top()
    sut.rmv(101)
    sut.add(5, 105, 15)
    assert 5 == sut.exec_top()
    assert 2 == sut.exec_top()

    # case 2.2:
    sut = TaskManager([[10, 26, 25]])
    sut.rmv(26)
    assert -1 == sut.exec_top()

    # case 2.3:
    sut = TaskManager([[6, 4, 48], [2, 7, 45], [6, 28, 44], [10, 27, 10]])
    assert 6 == sut.exec_top()
    sut.rmv(7)
    assert 6 == sut.exec_top()

    # case 2.4
    sut = TaskManager([[1, 1, 1]])
    sut.add(4, 104, 5)
    sut.rmv(104)
    sut.add(4, 104, 5)
    assert 4 == sut.exec_top()
    sut.add(5, 105, 2)
    assert 5 == sut.exec_top()
