# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        upper = p if p.val > q.val  else q
        lower = q if q.val < p.val else p
        node = root
        while node:
            if node.val < lower.val:
                node = node.right
            elif node.val > upper.val:
                node = node.left
            else:
                    return node
        return None

        