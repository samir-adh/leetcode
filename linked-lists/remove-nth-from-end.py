# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def remove(head: Optional[ListNode], prev: Optional[ListNode], node: ListNode):
            if not prev:
                return node.next
            prev.next = node.next
            return head
        
        p = None
        c = head
        q = head
        for _ in range(n):
            if not q:
                return 
            q = q.next
        while q:
            if not c:
                return
            p = c
            c = c.next
            q = q.next
        if not c :
            return
        return remove(head, p, c)


            
            
            
