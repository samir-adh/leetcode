from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = Deque([(p, q)])
        while len(stack) > 0:
            a, b = stack.pop()
            if a is None and b is None:
                continue
            if a is None or b is None:
                return False
            if a.val == b.val:
                stack.append((a.left, b.left))
                stack.append((a.right, b.right))
            else:
                return False
        return True