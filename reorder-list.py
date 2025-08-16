
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
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        if head.next is None:
            return

        n = 0
        current = head
        while current is not None:
            current = current.next
            n += 1

        half = n // 2
        head2 = head
        prev = None
        for i in range(half):
            prev = head2
            head2 = head2.next
        prev.next = None
        head2 = reverseList(head2)
        head = fuseLists(head, head2)


def reverseList(head: ListNode):
    previousNode = None
    currentNode = head
    nextNode = head.next
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode


def fuseLists(list1: Optional[ListNode], list2: Optional[ListNode]):
    head = list1
    needle = list1
    hand = list2
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    while True:
        if hand is None:
            break
        next_hand = needle.next
        needle.next = hand
        needle = hand
        hand = next_hand
    return head


def test_reverse():
    input_list = [1, 2, 3, 4]
    linked = toListNode(input_list)
    linked = reverseList(linked)
    print(linked.tolist())


def test_fuse():
    l1 = toListNode(
        [
            1,
            2,
            3,
        ]
    )
    l2 = toListNode([5, 6, 7])
    fused = fuseLists(l1, l2)
    print(fused.tolist())


def test_case1():
    case = toListNode([1, 2, 3, 4])
    Solution().reorderList(case)
    print(case.tolist())


if __name__ == "__main__":
    # test_fuse()
    # test_reverse()
    test_case1()
