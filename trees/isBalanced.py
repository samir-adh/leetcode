# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def dfs(node, balanced):
            if not balanced:
                return -1
            if node == None:
                return 0
            else:
                l= dfs(node.left, balanced)
                r = dfs(node.right, balanced)
                if abs(l-r) > 1:
                    balanced[0] = False
                return max(l,r) + 1
        dfs(root,balanced)
        return balanced[0]
