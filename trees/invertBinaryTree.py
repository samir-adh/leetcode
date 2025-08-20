# Definition for a binary tree node.
from collections import deque
from queue import Queue
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self.left and self.right == None:
            return f"{self.val}"
        else:
            return f"{self.val}\n\t{self.left}\n\t{self.right}"
        

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = Deque([root])
        while not len(stack) == 0:
            node = stack.pop()
            if node is None:
                continue
            left = node.left
            node.left = node.right
            node.right = left
            stack.append(node.left)
            stack.append(node.right)
        return root


