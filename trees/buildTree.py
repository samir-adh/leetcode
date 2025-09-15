# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        intable = {v:k for k,v in enumerate(inorder)}
        self.preIdx = 0
        left = 0
        right = len(preorder)

        def aux(l,r):
            if l>= r:
                return None
            nodeVal = preorder[self.preIdx]
            node = TreeNode(nodeVal)
            self.preIdx += 1
            node.left = aux(l, intable[nodeVal])
            node.right = aux(intable[nodeVal] + 1, r)
            return node
        
        return aux(left,right)