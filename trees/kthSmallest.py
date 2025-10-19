from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []
        i = 1
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop(-1)
            if i == k:
                return current.val
            else:
                i += 1
            current = current.right
        return 0
