from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        pass

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        pass

    def edit(self, task_id: int, new_priority: int) -> None:
        pass

    def rmv(self, task_id: int) -> None:
        pass

    def exec_top(self) -> int:
        pass


if __name__ == "__main__":
    sut = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    sut.add(4, 104, 5)
    sut.edit(102, 8)
    assert 3 == sut.exec_top()
    sut.rmv(101)
    sut.add(5, 105, 15)
    assert 5 == sut.exec_top()
