from typing import Optional

from .list_node import ListNode


class ConvertBinaryNumberInLinkedListToInteger:
    """
    Leetcode #1290
    Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
    """

    def get_decimal_value(self, head: Optional[ListNode]) -> int:
        p: Optional[ListNode] = head

        r: int = 0
        while p:
            t = p.val
            r <<= 1
            if t == 1:
                r += 1
            p = p.next

        return r
