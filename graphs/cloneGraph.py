from typing import Optional, List


class Node:
    """Definition for a Node."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: List["Node"] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        queue = [node]
        table = {node: Node(node.val)}
        while queue:
            current = queue.pop()
            clone = table[current]
            for child in current.neighbors:
                if child not in table:
                    table[child] = Node(child.val)
                    queue.append(child)
                clone.neighbors.append(table[child])
        return table[node]
