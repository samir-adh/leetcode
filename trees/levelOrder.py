from typing import Deque, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
List = list

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        traversal = []
        queue = Deque([(root,0)])
        while queue:
            node, depth = queue.pop()
            if len(traversal) <= depth:
                traversal.append([])
            traversal[depth].append(node.val)
            if node.left:
                queue.appendleft((node.left,depth+1))
            if node.right:
                queue.appendleft((node.right,depth+1))
        return traversal

        