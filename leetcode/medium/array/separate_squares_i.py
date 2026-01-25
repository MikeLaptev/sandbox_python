from typing import List


class SeparateSquaresI:
    """
    Leetcode #3453
    Link: https://leetcode.com/problems/separate-squares-i/
    """

    def separate_squares(self, squares: List[List[int]]) -> float:
        """
        >>> sut = SeparateSquaresI()
        >>> expected = 2.00000
        >>> actual = sut.separate_squares([[0, 0, 2], [0, 0, 1], [2, 2, 2], [2, 2, 1]])
        >>> assert 10 ** (-5) > abs(actual - expected), f"expected: {expected}, actual: {actual}; diff: {abs(actual - expected)}"
        >>> expected = 0.00000
        >>> actual = sut.separate_squares([[0, 0, 2], [0, 0, 1], [-2, -2, 2], [-1, -1, 1]])
        >>> assert 10 ** (-5) > abs(actual - expected), f"expected: {expected}, actual: {actual}; diff: {abs(actual - expected)}"
        >>> expected = 1.16667
        >>> actual = sut.separate_squares([[1, 1, 1], [0, 0, 2]])
        >>> assert 10 ** (-5) > abs(actual - expected), f"expected: {expected}, actual: {actual}; diff: {abs(actual - expected)}"
        >>> expected = 19.95000
        >>> actual = sut.separate_squares([[8, 16, 1], [6, 15, 10]])
        >>> assert 10 ** (-5) > abs(actual - expected), f"expected: {expected}, actual: {actual}; diff: {abs(actual - expected)}"
        >>> expected = 1.00000
        >>> actual = sut.separate_squares([[0, 0, 1], [2, 2, 1]])
        >>> assert 10 ** (-5) > abs(actual - expected), f"expected: {expected}, actual: {actual}; diff: {abs(actual - expected)}"
        >>> expected = 954521423.8020256
        >>> actual = sut.separate_squares([[522261215, 954313664, 225462], [628661372, 718610752, 10667], [619734768, 941310679, 44788], [352367502, 656774918, 289036], [860247066, 905800565, 100123], [817623994, 962847576, 71460], [691552058, 782740602, 36271], [911356, 152015365, 513881], [462847044, 859151855, 233567], [672324240, 954509294, 685569]])
        >>> assert 10 ** (-5) > abs(actual - expected), f"expected: {expected}, actual: {actual}; diff: {abs(actual - expected)}"
        """
        min_y, max_y, total_area = squares[0][1], squares[0][1], 0
        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)
            min_y = min(min_y, y)

        lo, hi = min_y, max_y
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = lo + (hi - lo) / 2
            if self.__check(squares=squares, total_area=total_area, limit_y=mid):
                hi = mid
            else:
                lo = mid

        return hi

    def __check(
        self, squares: List[List[int]], total_area: int, limit_y: float
    ) -> bool:
        area = 0
        for x, y, l in squares:
            if y < limit_y:
                area += l * min(limit_y - y, l)
        return area >= total_area / 2


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
