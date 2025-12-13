import re
from collections import defaultdict
from turtledemo.minimal_hanoi import Disc
from typing import List, Set, Tuple


class CouponCodeValidator:
    """
    Leetcode #3606
    Link: https://leetcode.com/problems/coupon-code-validator
    """

    __valid_business_lines: List[str] = [
        "electronics",
        "grocery",
        "pharmacy",
        "restaurant",
    ]

    def validate_coupons(
        self, code: List[str], business_line: List[str], is_active: List[bool]
    ) -> List[str]:
        """
        >>> sut = CouponCodeValidator()
        >>> expected = ["PHARMA5", "SAVE20"]
        >>> actual = sut.validate_coupons(code = ["SAVE20", "", "PHARMA5", "SAVE@20"], \
                                       business_line = ["restaurant", "grocery", "pharmacy", "restaurant"], \
                                       is_active = [True, True, True, True])
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        >>> expected = ["ELECTRONICS_50"]
        >>> actual = sut.validate_coupons(code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"], \
                                       business_line = ["grocery", "electronics", "invalid"], \
                                       is_active = [False, True, True])
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        >>> expected = ["PHARMA5", "SAVE20"]
        >>> actual = sut.validate_coupons(code = ["SAVE20", "", "PHARMA5", "SAVE@20"], \
                                       business_line = ["restaurant", "grocery", "pharmacy", "restaurant"], \
                                       is_active = [True, True, True, True])
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        >>> expected = ["j", "j", "P"]
        >>> actual = sut.validate_coupons(code = ["P", "j", "x", "c", "j", "C", "G"], \
                                       business_line = ["pharmacy", "electronics", "invalid", "restaurant", "electronics", "pharmacy", "restaurant"], \
                                       is_active = [True, True, False, False, True, False, False])
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        """
        preprocessing: defaultdict[str, List[str]] = defaultdict(list)

        for i in range(len(code)):
            if business_line[i] not in self.__valid_business_lines or not is_active[i]:
                continue
            if re.match(r"^\w+$", code[i]):
                preprocessing[business_line[i]].append(code[i])

        result: List[str] = []
        for business_line in self.__valid_business_lines:
            if business_line in preprocessing:
                result += sorted(preprocessing[business_line])

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
