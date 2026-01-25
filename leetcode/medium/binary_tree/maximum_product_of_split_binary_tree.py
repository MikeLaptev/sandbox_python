from functools import cache
from typing import Optional, List, Tuple, Set, Self

from leetcode.medium.binary_tree.tree_node import TreeNode


class MaximumProductOfSplitBinaryTree:
    """
    Leetcode #1339
    Link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
    """

    def max_product(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res: Optional[int] = None

        # getting overall sum
        total_sum: int = self.__get_sum_of_subtree(root)

        queue: List[TreeNode] = [root]
        while queue:
            current: TreeNode = queue.pop(0)
            # if we remove a branch between current and left child
            if current.left:
                queue.append(current.left)
                t: int = self.__get_sum_of_subtree(current.left)
                product: int = (total_sum - t) * t
                if not res or res < product:
                    res = product
            # if we remove a branch between current and right child
            if current.right:
                queue.append(current.right)
                t: int = self.__get_sum_of_subtree(current.right)
                product: int = (total_sum - t) * t
                if not res or res < product:
                    res = product

        return (res % (10**9 + 7)) if res is not None else 0

    @cache
    def __get_sum_of_subtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total_sum: int = root.val
        if root.left:
            total_sum += self.__get_sum_of_subtree(root.left)
        if root.right:
            total_sum += self.__get_sum_of_subtree(root.right)

        return total_sum

    def max_product_opt(self, root: Optional[TreeNode]) -> int:
        vals = []

        def fn(node):
            if not node:
                return 0
            ans = node.val + fn(node.left) + fn(node.right)
            vals.append(ans)
            return ans

        total = fn(root)
        return max((total - x) * x for x in vals) % 1_000_000_007
