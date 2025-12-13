from typing import List


class CountMentionsPerUser:
    """
    Leetcode #3433
    Link: https://leetcode.com/problems/count-mentions-per-user
    """

    def count_mentions(
        self, number_of_users: int, events: List[List[str]]
    ) -> List[int]:
        """
        >>> sut = CountMentionsPerUser()
        >>> actual = sut.count_mentions(number_of_users = 2, events = [["MESSAGE","10","id1 id0"], ["OFFLINE","11","0"], ["MESSAGE","71","HERE"]])
        >>> assert [2, 2] == actual, f"expected: [2, 2]; got: {actual}"
        >>> actual = sut.count_mentions(number_of_users = 2, events = [["MESSAGE","10","id1 id0"], ["OFFLINE","11","0"], ["MESSAGE","12","ALL"]])
        >>> assert [2, 2] == actual, f"expected: [2, 2]; got: {actual}"
        >>> actual = sut.count_mentions(number_of_users = 2, events = [["OFFLINE","10","0"], ["MESSAGE","12","HERE"]])
        >>> assert [0, 1] == actual, f"expected: [0, 1]; got: {actual}"
        """
        result: List[int] = [0] * number_of_users

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
