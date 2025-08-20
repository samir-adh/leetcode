from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialisation
        prev = None
        current = head
        tip = head
        if head is None:
            return None
        for _ in range(n):
            if tip is None:
                raise Exception("tip was set to None during initialisation")
            tip = tip.next

        # Loop
        while tip is not None:
            if current is None:
                raise Exception("current was set to None during the loop")
            prev = current
            current = current.next
            tip = tip.next
        if current is None:
            raise Exception("current was set to None during the loop")
        
        if prev is None:
            return current.next

        # Remove node
        prev.next = current.next
        return head


def test_case1():
    head = toListNode([1, 2, 3, 4, 5])
    n = 2
    expected = toListNode([1, 2, 3, 5])
    out = Solution().removeNthFromEnd(head, n)
    if expected is None or out is None:
        assert expected == out
    else:
        assert out.tolist() == expected.tolist()


def test_case2():
    head = toListNode([1])
    n = 1
    expected = toListNode([])
    out = Solution().removeNthFromEnd(head, n)
    if expected is None or out is None:
        assert expected == out
    else:
        assert out.tolist() == expected.tolist()


def test_case3():
    head = toListNode([1, 2])
    n = 1
    expected = toListNode([1])
    out = Solution().removeNthFromEnd(head, n)
    if expected is None or out is None:
        assert expected == out
    else:
        assert out.tolist() == expected.tolist()


def test_case4():
    head = toListNode([1, 2])
    n = 2
    expected = toListNode([2])
    out = Solution().removeNthFromEnd(head, n)
    if expected is None or out is None:
        assert expected == out
    else:
        assert out.tolist() == expected.tolist()

def test_case5():
    head = toListNode([1, 2,3])
    n = 3
    expected = toListNode([2,3])
    out = Solution().removeNthFromEnd(head, n)
    if expected is None or out is None:
        assert expected == out
    else:
        assert out.tolist() == expected.tolist()


if __name__ == "__main__":
    test_case3()
