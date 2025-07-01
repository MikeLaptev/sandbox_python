from typing import Optional, Deque, Tuple

from .tree_node import TreeNode
from collections import deque


class SumRootToLeafNumbers:
    """
    Leetcode #129
    Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
    """

    def sum_numbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q: Deque[Tuple[TreeNode, int]] = deque()
        q.append((root, root.val))
        r = 0
        while q:
            c = q.popleft()
            if not c[0].left and not c[0].right:
                r += c[1]
                continue

            if c[0].left:
                q.append((c[0].left, c[0].left.val + c[1] * 10))
            if c[0].right:
                q.append((c[0].right, c[0].right.val + c[1] * 10))
        return r
