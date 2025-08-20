from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, balanced) -> int:
            if not balanced[0]:
                return -1
            if node is None:
                return 0
            else:
                left = dfs(node.left, balanced)
                right = dfs(node.right, balanced)
                if abs(left - right) > 1:
                    balanced[0] = False
                return max(left, right) + 1

        balanced = [True]
        dfs(root, balanced)
        return balanced[0]
