from typing import Optional, List

from leetcode.medium.binary_tree.tree_node import TreeNode


class MaximumLevelSumOfBinaryTree:
    """
    Leetcode #1161
    Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
    """

    def max_level_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        layer_id: int = 1
        result_id: int = -1
        result: int = 0
        queue: List[TreeNode] = [root]
        layer: List[TreeNode] = []
        while True:
            k: int = len(queue)
            while k > 0:
                e = queue.pop(0)
                layer.append(e)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
                k -= 1

            if not layer:
                break
            t: int = sum([e.val for e in layer])
            if result_id == -1 or t > result:
                result = t
                result_id = layer_id
            layer_id += 1
            layer = []

        return result_id
