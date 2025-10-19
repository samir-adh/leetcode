from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        intable = {k: v for v, k in enumerate(inorder)}
        preIdx = 0

        def aux(left: int, right: int):
            nonlocal preIdx
            if left >= right:
                return None
            curr = preorder[preIdx]
            node = TreeNode(val=curr)
            k = intable[curr]
            preIdx += 1
            node.left = aux(left, k)
            node.right = aux(k + 1, right)
            return node

        return aux(0, len(preorder))
