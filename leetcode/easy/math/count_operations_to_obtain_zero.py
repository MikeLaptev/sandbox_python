class CountOperationsToObtainZero:
    """
    Leetcode #2169
    Link: https://leetcode.com/problems/count-operations-to-obtain-zero
    """

    def count_operations(self, num1: int, num2: int) -> int:
        """
        >>> sut = CountOperationsToObtainZero()
        >>> assert 3 == sut.count_operations(2, 3)
        >>> assert 1 == sut.count_operations(10, 10)
        """
        counter = 0

        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            counter += 1

        return counter

    def count_operations_recursive(self, num1: int, num2: int) -> int:
        """
        >>> sut = CountOperationsToObtainZero()
        >>> assert 3 == sut.count_operations_recursive(2, 3)
        >>> assert 1 == sut.count_operations_recursive(10, 10)
        """
        if num1 == 0 or num2 == 0:
            return 0
        elif num1 < num2:
            return self.count_operations_recursive(num2, num1)
        else:
            return num1 // num2 + self.count_operations_recursive(num2, num1 % num2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
