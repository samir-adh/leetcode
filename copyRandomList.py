from typing import Optional


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def tolist(self):
        current = self
        out = []
        while current is not None:
            out.append(current.val)
            current = current.next
        return out


def toListNode(input_list: list):
    if len(input_list) == 0:
        return None
    head = Node(input_list[0])
    current = head
    for item in input_list[1:]:
        current.next = Node(item)
        current = current.next
    return head


class Solution:
    def copyRandomList(self, head:' Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        table: dict[Node,Node] = {}
        current = head.next

        while current is not None:
            new_node = Node(current.val, None, None)
            table[current] = new_node
        
        current = head
        new_head = table[head]

        while current is not None:
            rd = current.random
            nx = current.next
            table[current].next = table[nx] if nx is not None else None
            table[current].random = table[rd] if rd is not None else None 
            current=current.next
        
        return new_head


