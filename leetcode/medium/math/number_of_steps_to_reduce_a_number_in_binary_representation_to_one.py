class NumberOfStepsToReduceNumberInBinaryRepresentationToOne:
    """
    Leetcode #1404
    Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
    """

    def num_steps(self, s: str) -> int:
        """
        >>> sut = NumberOfStepsToReduceNumberInBinaryRepresentationToOne()
        >>> assert 3 == sut.num_steps('11'), f"expected: 3, got: {sut.num_steps('11')}"
        >>> assert 1 == sut.num_steps('10'), f"expected: 1, got: {sut.num_steps('10')}"
        >>> assert 0 == sut.num_steps('1'), f"expected: 0, got: {sut.num_steps('1')}"
        >>> assert 6 == sut.num_steps('11000'), f"expected: 6, got: {sut.num_steps('11000')}"
        >>> assert 6 == sut.num_steps('1101'), f"expected: 6, got: {sut.num_steps('1101')}"
        """
        steps: int = 0

        flip: bool = False
        for i in range(len(s) - 1, -1, -1):
            if i == 0 and not flip:
                break
            c: str = s[i]
            if c == "0":  # even
                if flip:  # become odd
                    flip = False
                else:
                    # divide by two
                    steps += 1
                    continue
            # odd
            if flip:
                # preserve the flip & divide by two
                steps += 1
            else:
                steps += 2  # adding one (become even) & divide by two
                flip = True

        return steps


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
