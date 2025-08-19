# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def aux(node: Optional[TreeNode]):
            nonlocal diameter
            if node is None:
                return 0

            leftHeight = aux(node.left)
            rightHeight = aux(node.right)

            diameter = max(leftHeight + rightHeight, diameter)
            return max(leftHeight, rightHeight) + 1

        aux(root)
        return diameter
