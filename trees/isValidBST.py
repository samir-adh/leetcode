from math import inf
from typing import Optional, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = Deque([(root, -inf, +inf)])
        while queue:
            node, minval, maxval = queue.pop()
            if not (minval < node.val < maxval):
                return False
            if node.left:
                upper = min(node.val, maxval)
                queue.appendleft((node.left, minval, upper))
            if node.right:
                lower = max(node.val, minval)
                queue.appendleft((node.right, lower, maxval))
            
        return True
