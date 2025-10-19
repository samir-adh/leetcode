# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        traversal = []
        current = root
        if not root:
            return traversal
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            traversal.append(current.val)
            current = current.right
        return traversal
                