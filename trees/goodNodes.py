from typing import Optional, Deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = Deque([(root,root.val)])
        count = 0
        while queue:
            node, maxval = queue.pop()
            if node.val >= maxval:
                count+=1
            maxval= max(node.val, maxval)
            if node.left:
                queue.appendleft((node.left,maxval ))
            if node.right:
                queue.appendleft((node.right, maxval))
        return count
        