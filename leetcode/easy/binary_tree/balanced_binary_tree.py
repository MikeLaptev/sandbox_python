from typing import Optional

from leetcode.easy.binary_tree.tree_node import TreeNode


class BalancedBinaryTree:
    """
    Leetcode #110
    Link: https://leetcode.com/problems/balanced-binary-tree
    """

    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return (
            self.is_balanced(root.left)
            and self.is_balanced(root.right)
            and abs(self.height(root.left) - self.height(root.right)) <= 1
        )

    def height(self, root: Optional[TreeNode]) -> int:
        return (
            0
            if root is None
            else 1 + max(self.height(root.left), self.height(root.right))
        )


if __name__ == "__main__":
    sut = BalancedBinaryTree()

    # case -1
    n1: TreeNode = TreeNode(1)
    n2: TreeNode = TreeNode(2)
    n3: TreeNode = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n4: TreeNode = TreeNode(4)
    n5: TreeNode = TreeNode(5)
    n2.left = n4
    n2.right = n5
    n6: TreeNode = TreeNode(6)
    n3.left = n6
    n8: TreeNode = TreeNode(8)
    n4.right = n8

    assert True == sut.is_balanced(n1)

    # case 0
    n1: TreeNode = TreeNode(1)
    n2: TreeNode = TreeNode(2)
    n3: TreeNode = TreeNode(3)
    n1.left = n2
    n2.left = n3

    assert False == sut.is_balanced(n1)

    # case 1
    n1: TreeNode = TreeNode(3)
    n2: TreeNode = TreeNode(9)
    n3: TreeNode = TreeNode(20)
    n1.left = n2
    n1.right = n3
    n4: TreeNode = TreeNode(7)
    n5: TreeNode = TreeNode(15)
    n3.left = n5
    n3.right = n4

    assert True == sut.is_balanced(n1)

    # case 2
    n1: TreeNode = TreeNode(1)
    n2: TreeNode = TreeNode(2)
    n3: TreeNode = TreeNode(2)
    n1.left = n2
    n1.right = n3
    n4: TreeNode = TreeNode(3)
    n5: TreeNode = TreeNode(3)
    n3.left = n4
    n3.right = n5
    n6: TreeNode = TreeNode(4)
    n7: TreeNode = TreeNode(4)
    n5.left = n6
    n5.right = n7

    assert False == sut.is_balanced(n1)

    # case 3
    assert True == sut.is_balanced(None)
