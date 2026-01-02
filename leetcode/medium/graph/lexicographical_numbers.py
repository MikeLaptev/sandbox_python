from typing import List


class LexicographicalNumbers:
    """
    Leetcode #386
    Link: https://leetcode.com/problems/lexicographical-numbers

    We can do the same thing iterative, the overall concept remains the same as DFS approach.
    The difference will be how we organize and implement it.

    We initialize the current number as 1, which is the first number in lexicographical order,
    and set up a loop that runs n times because we want to generate exactly n numbers.

    In each iteration, we add the current number to the result list. After that, we check
    if we can go deeper by multiplying the current number by 10, appending a zero to the current number,
    giving us the lexicographically smallest possible next number. If the result is still less
    than or equal to n, we update the current number to this new value and continue.

    If multiplying by 10 would exceed n, we increment the current number. However, this
    increment can’t always happen directly. If the current number ends in 9 or goes beyond
    the next "root" (like moving from 19 to 2), we divide by 10 to move up a level and
    strip off the last digit. This way we make sure we don’t skip any numbers.

    After incrementing, if the new current number ends in a zero (like 20), we continue
    removing zeroes, dividing by 10, until we get a valid number. This ensures we stay
    in lexicographical order as we move forward.

    This way, we mimic the way we would manually write numbers in lexicographical order.
    We move from one number to the next by considering when to go deeper (appending digits) and
    when to backtrack (moving to the next root). Unlike the recursive method, which explores
    each branch of the binary_tree by diving deeper, this method keeps track of the current number and
    directly adjusts it. This makes it more space-efficient, with essentially no extra space
    overhead, and runs in O(n) time.
    """

    def lexical_order(self, n: int) -> List[int]:
        """
        >>> sut = LexicographicalNumbers()
        >>> expected = [1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,4,5,6,7,8,9]
        >>> actual = sut.lexical_order(34)
        >>> assert expected == actual, actual
        >>> expected = [1,10,11,12,13,2,3,4,5,6,7,8,9]
        >>> actual = sut.lexical_order(13)
        >>> assert expected == actual, actual
        >>> expected = [1, 2]
        >>> actual = sut.lexical_order(2)
        >>> assert expected == actual, actual
        """
        result = []
        c = 1

        for _ in range(n):
            result.append(c)

            if c * 10 <= n:
                c *= 10
            else:
                while c % 10 == 9 or c >= n:
                    c //= 10
                c += 1

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
