from typing import Optional
from .list_node import ListNode


class ReverseLinkedListII:
    """
    Leetcode #92
    Link: https://leetcode.com/problems/reverse-linked-list-ii/
    """

    def reverse_between(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        >>> sut = ReverseLinkedListII()
        >>> n1 = ListNode(1)
        >>> n2 = ListNode(2)
        >>> n1.next = n2
        >>> n3 = ListNode(3)
        >>> n2.next = n3
        >>> n4 = ListNode(4)
        >>> n3.next = n4
        >>> n5 = ListNode(5)
        >>> n4.next = n5
        >>> actual = sut.reverse_between(n1, 2, 4)
        """
        t: ListNode = ListNode(next=head)
        prev: Optional[ListNode] = t
        for _ in range(1, left):
            prev = prev.next
        curr: Optional[ListNode] = prev.next
        for _ in range(right - left):
            # tmp overwritten by next node to be moved
            tmp = curr.next
            # rerouting links
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        return t.next


if __name__ == "__main__":
    import doctest

    doctest.testmod()
