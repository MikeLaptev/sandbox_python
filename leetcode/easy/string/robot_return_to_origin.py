class RobotReturnToOrigin:
    """
    Leetcode #657
    Link: https://leetcode.com/problems/robot-return-to-origin/description
    """

    def judge_circle(self, moves: str) -> bool:
        """
        >>> sut = RobotReturnToOrigin()
        >>> moves: str = "UD"
        >>> assert True == sut.judge_circle(moves)
        >>> moves: str = "LL"
        >>> assert False == sut.judge_circle(moves)
        """
        h, v = 0, 0
        for move in moves:
            match move:
                case "U":
                    h += 1
                case "D":
                    h -= 1
                case "L":
                    v += 1
                case "R":
                    v -= 1

        return h == 0 and v == 0

    def judge_circle_opt(self, moves: str) -> bool:
        """
        >>> sut = RobotReturnToOrigin()
        >>> moves: str = "UD"
        >>> assert True == sut.judge_circle(moves)
        >>> moves: str = "LL"
        >>> assert False == sut.judge_circle(moves)
        """
        h: bool = moves.count("L") == moves.count("R")
        v: bool = moves.count("U") == moves.count("D")
        return v and h


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
