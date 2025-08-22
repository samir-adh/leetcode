# Definition for a binary tree node.
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

        stack = Deque([root])
        if subRoot is None:
            return True
        while len(stack) > 0:
            tree = stack.pop()
            if tree is None :
                continue
            if isSameTree(tree, subRoot):
                return True
            else:
                stack.append(tree.left)
                stack.append(tree.right)
            
        return False