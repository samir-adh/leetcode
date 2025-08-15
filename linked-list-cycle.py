# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode | None = None


def to_linked_list(x: list, pos: int):
    head = ListNode(x[0])
    current = head
    loop_node = None
    for i in range(1, len(x)):
        current.next = ListNode(x[i])
        if i == pos:
            loop_node = current
        current = current.next
    current.next = loop_node
    return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        start = head
        end = start.next

        while end is not None and end.next is not None:
            if end == start:
                return True
            start = start.next
            end = end.next.next
        return False


def test_case1():
    instance = to_linked_list([3, 2, 0, -4], 1)
    expected = True
    answer = Solution().hasCycle(instance)

    assert answer == expected, f"Expected {expected} got {answer}"
