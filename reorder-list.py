from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def tolist(self):
        current = self
        out = []
        while current != None:
            out.append(current.val)
            current = current.next
        return out


def toListNode(input_list: list):
    head = ListNode(input_list[0])
    current = head
    for item in input_list[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        n = 0
        current = head
        while current is not None:
            current = current.next
            n+=1

        half = n//2

        current = head
        for i in range(half):
            current = current.next
        
        head2 = current.next
        current.next = None

        head2 = reverseList(head2)
        head = fuseLists(head, head2)



def reverseList(head: ListNode):
    prev = None
    current = head
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev


def fuseLists(head1: ListNode, head2: ListNode):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    needle = head1
    hand = head2
    while hand is not None:
        next_hand = needle.next
        needle.next = hand
        needle = hand
        hand = next_hand

    return head1


def test_reverse():
    input_list = [1, 2, 3, 4]
    linked = toListNode(input_list)
    linked = reverseList(linked)
    print(linked.tolist())


def test_fuse():
    l1 = toListNode([1, 2, 3])
    l2 = toListNode([5, 6, 7])
    fused = fuseLists(l1, l2)
    print(fused.tolist())


def test_case1():
    case = toListNode([1, 2, 3, 4])
    Solution().reorderList(case)
    print(case.tolist())


if __name__ == "__main__":
    test_fuse()
    test_reverse()
    test_case1()
