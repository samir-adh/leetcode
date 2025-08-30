from typing import Optional, Deque, OrderedDict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        visitedNodes =set()
        visitedVals = []
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left not in visitedNodes:
                stack.append(node.left)
            else:
                visitedNodes.add(node)
                visitedVals.append(node.val)
                if len(visitedVals) ==k:
                    return visitedVals[-1]
                stack.pop()
                if node.right:
                    stack.append(node.right)
        return visitedVals[k-1]