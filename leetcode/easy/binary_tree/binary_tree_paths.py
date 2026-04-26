from typing import Optional, List, Tuple

from leetcode.easy.binary_tree.tree_node import TreeNode


class BinaryTreePaths:
    """
    Leetcode #257
    Link: https://leetcode.com/problems/binary-tree-paths/description/
    """

    def binary_tree_paths(self, root: Optional[TreeNode]) -> List[str]:
        paths: List[str] = []
        if root is None:
            return paths

        queue: List[Tuple[TreeNode, str]] = [(root, "")]
        while queue:
            node, path = queue.pop(0)
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
                continue
            if node.left:
                queue.append((node.left, path + "->"))
            if node.right:
                queue.append((node.right, path + "->"))

        return paths
