# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, diameter):
            if node == None:
                return 0
            else :
                left = dfs(node.left, diameter)
                right = dfs(node.right, diameter)
                diameter[0] = max(diameter[0], left + right)
                return max(left, right) + 1
        diameter = [0]
        dfs(root, diameter)
        return diameter[0]