from collections import deque
from typing import Optional, Deque, Tuple

from leetcode.easy.binary_tree.tree_node import TreeNode


class SumOfRootToLeafBinaryNumbers:
    """
    Leetcode #1022
    Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
    """

    def sum_root_to_leaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        r: int = 0

        q: Deque[Tuple[TreeNode, int]] = deque()
        q.append((root, root.val))
        while q:
            c: Tuple[TreeNode, int] = q.popleft()
            if not c[0].left and not c[0].right:
                r += c[1]
                continue
            if c[0].left:
                q.append((c[0].left, (c[1] << 1) + c[0].left.val))
            if c[0].right:
                q.append((c[0].right, (c[1] << 1) + c[0].right.val))

        return r
