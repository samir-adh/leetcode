# Definition for a binary tree node.
from typing import Deque, Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = Deque([(root,0)])
        view = []
        while queue:
            node, depth = queue.pop()
            if len(view) <= depth:
                view.append(node.val)
            else:
                view[depth] = node.val
            if node.left:
                queue.appendleft((node.left, depth+1))
            if node.right:
                queue.appendleft((node.right,depth+1))
        return view
        