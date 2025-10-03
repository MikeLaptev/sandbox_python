class StudentAttendanceRecordI:
    """
    Leetcode #551
    Link: https://leetcode.com/problems/student-attendance-record-i
    """

    def check_record(self, s: str) -> bool:
        """
        >>> sut = StudentAttendanceRecordI()
        >>> s = "PPALLP"
        >>> assert True == sut.check_record(s), "incorrect for PPALLP"
        >>> s = "PPALLL"
        >>> assert False == sut.check_record(s), "incorrect for PPALLL"
        """
        return s.count("A") < 2 and s.count("LLL") == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
