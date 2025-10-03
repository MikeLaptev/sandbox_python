import math
from typing import List, Dict


class LargestTriangleArea:
    """
    Leetcode #812
    Link: https://leetcode.com/problems/largest-triangle-area
    """

    def largest_triangle_area(self, points: List[List[int]]) -> float:
        p2p: Dict[int, Dict[int, float]] = {i: {} for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p2p[i][j] = self.__distance(points[i], points[j])

        largest = -1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    v = self.__squared_square(p2p[i][j], p2p[i][k], p2p[j][k])
                    if v > largest:
                        largest = v

        if largest >= 0:
            return math.sqrt(largest)
        return -1

    def __distance(self, a: List[int], b: List[int]) -> float:
        return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))

    def __squared_square(self, a: float, b: float, c: float) -> float:
        s = (a + b + c) / 2
        return s * (s - a) * (s - b) * (s - c)

    def largest_triangle_area_opt(self, points: List[List[int]]) -> float:
        largest = 0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    if largest < area:
                        largest = area

        return largest / 2.0
