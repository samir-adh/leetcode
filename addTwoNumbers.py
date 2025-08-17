from math import remainder
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next

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
    head = ListNode(input_list[0])
    current = head
    for item in input_list[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        node = head
        current1 = l1
        current2 = l2
        ret = 0
        while not (current1 is None and current2 is None):
            x = ret
            if current1 is not None:
                x += current1.val
                current1 = current1.next
            if current2 is not None:
                x += current2.val
                current2 = current2.next

            val = x % 10
            ret = x // 10
            node.val = val
            if  current1 is None and current2 is None:
                if ret != 0:
                    node.next = ListNode(ret)
                break
            nextnode = ListNode(0)
            node.next = nextnode
            node = nextnode
        
        return head
