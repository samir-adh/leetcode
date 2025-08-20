# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node, diameter ):
            if node is None:
                return 0
            else :
                leftHeight = height(node.left, diameter)
                rightHeight = height(node.right, diameter)
                diameter[0] = max(diameter[0], leftHeight+rightHeight)
                return max(leftHeight, rightHeight) + 1
        diameter = [0]
        height(root, diameter)
        return diameter[0]
