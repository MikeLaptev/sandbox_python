from typing import Optional, List, Tuple

from leetcode.easy.tree.tree_node import TreeNode


class BinaryTreePostorderTraversal:
    """
    Leetcode #145
    Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
    """

    def postorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        postorder: List[int] = []
        if root.left:
            postorder += self.postorder_traversal_recursive(root.left)
        if root.right:
            postorder += self.postorder_traversal_recursive(root.right)
        postorder.append(root.val)

        return postorder

    def postorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        postorder: List[int] = []
        stack = [(root, False)]
        while stack:
            t: Tuple[TreeNode, bool] = stack.pop()
            if t[1]:
                postorder.insert(0, t[0].val)
            else:
                if t[0].left:
                    stack.append((t[0].left, False))
                if t[0].right:
                    stack.append((t[0].right, False))
                stack.append((t[0], True))

        return postorder
