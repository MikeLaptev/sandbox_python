# Definition for a binary tree node.
from typing import Optional, Self


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None
    ):
        self.val = val
        self.left = left
        self.right = right
