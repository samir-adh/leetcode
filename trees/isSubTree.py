# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            else:
                return sameTree(p.left,q.left) and sameTree(p.right, q.right)
        def aux(root: Optional[TreeNode], sub: TreeNode):
            if root is None:
                return False
            if sameTree(root, sub):
                return True
            else:
                return aux(root.left,sub) or aux(root.right,sub)
        return aux(root, subRoot) 


        