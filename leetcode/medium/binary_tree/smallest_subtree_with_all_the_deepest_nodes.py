from collections import deque
from typing import Optional, List, Tuple

from leetcode.medium.binary_tree.tree_node import TreeNode


class SmallestSubtreeWithAllTheDeepestNodes:
    """
    Leetcode #1123
    Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

    Leetcode #865
    Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description
    """

    def subtree_with_all_deepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        longest_paths: List[List[TreeNode]] = []
        longest_path_length: int = 0
        queue: List[List[TreeNode]] = [[root]]
        while queue:
            current = queue.pop(0)

            # if a possible deepest node (leaf)
            if not current[-1].left and not current[-1].right:
                if len(current) == longest_path_length:
                    longest_paths.append(current)
                elif len(current) > longest_path_length:
                    longest_paths.clear()
                    longest_paths.append(current)
                    longest_path_length = len(current)
                continue

            if current[-1].left:
                queue.append(current + [current[-1].left])
            if current[-1].right:
                queue.append(current + [current[-1].right])

        if len(longest_paths) == 1:
            return longest_paths[0][-1]

        n = longest_paths[0][0]
        for i in range(longest_path_length - 1, -1, -1):
            k = longest_paths[0][i]
            all_the_same: bool = True
            for longest_path in longest_paths:
                if longest_path[i] != k:
                    all_the_same = False
            if all_the_same:
                return k
            n = k

        return n

    def lca_deepest_leaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None  # (depth, lca)
            l, l_lca = dfs(node.left)
            r, r_lca = dfs(node.right)
            if l == r:
                return l + 1, node
            return (l + 1, l_lca) if l > r else (r + 1, r_lca)

        return dfs(root)[1]
