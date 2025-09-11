from typing import Optional

from .list_node import ListNode


class ReverseList:
    """
    Leetcode #206
    Link: https://leetcode.com/problems/reverse-linked-list/
    """

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        p = None
        c = head

        while c.next is not None:
            t = c.next
            c.next = p
            p = c
            c = t
        c.next = p

        return c
