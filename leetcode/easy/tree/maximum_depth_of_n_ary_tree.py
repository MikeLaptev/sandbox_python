from typing import Tuple, List

from leetcode.easy.tree.node import Node


class MaximumDepthOfNaryTree:
    """
    Leetcode #559
    Link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
    """

    def max_depth_iterative(self, root: Node) -> int:
        if root is None:
            return 0
        r: int = -1
        queue: List[Tuple[Node, int]] = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if depth > r:
                r = depth
            for child in node.children:
                queue.append((child, depth + 1))

        return r

    def max_depth_recursive(self, root: Node) -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.max_depth_recursive(child) for child in root.children)
