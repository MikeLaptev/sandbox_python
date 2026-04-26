from itertools import count
from typing import List, Set


class ReportSpamMessage:
    """
    Leetcode #3295
    Link: https://leetcode.com/problems/report-spam-message/description/
    """

    def report_spam(self, message: List[str], banned_words: List[str]) -> bool:
        """
        >>> sut = ReportSpamMessage()
        >>> message: List[str] = ["hello","programming","fun"]
        >>> banned_words: List[str] = ["world","programming","leetcode"]
        """
        bw: Set[str] = set(banned_words)
        count: int = 0
        for word in message:
            if word in bw:
                if count == 1:
                    return True
                count += 1
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
