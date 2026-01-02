from typing import List


class PlusOne:
    """
    Leetcode #66
    Link: https://leetcode.com/problems/plus-one/
    """

    def plus_one(self, digits: List[int]) -> List[int]:
        """
        >>> sut = PlusOne()
        >>> expected = [1, 2, 4]
        >>> actual = sut.plus_one([1, 2, 3])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = [4, 3, 2, 2]
        >>> actual = sut.plus_one([4, 3, 2, 1])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = [1, 0, 0]
        >>> actual = sut.plus_one([9, 9])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        answer: List[int] = []
        shift: bool = False
        is_first: bool = True
        for i, d in enumerate(reversed(digits)):
            r: int = d
            if is_first:
                r += 1
                is_first = False
            if shift:
                r += 1
                shift = False
            if r >= 10:
                shift = True
                r -= 10
            answer.append(r)

        if shift:
            answer.append(1)

        return list(reversed(answer))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
