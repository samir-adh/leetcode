from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):  # type: ignore
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        table = {}
        current = head
        while current is not None:
            node = Node(current.val)
            table[current] = node
            current = current.next

        current = head
        newHead = table[current]

        while current is not None:
            node = table[current]
            node.next = table.get(current.next)
            node.random = table.get(current.random)
            current = current.next

        return newHead
