class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

    def __str__(self):
        current = self
        output = "["
        while current:
            output += f"{current.val}->"
            current = current.next
        return output[:-2] + "]"

    def to_arr(self):
        current = self
        output = []
        while current:
            output.append(current.val)
            current = current.next
        return output


# i think we can use a heap to store the  first element of each list
# at each step we pop the head of the heap and append it to out new linkedlist
# then we push the .next of the popped item to the heap
# Definition for singly-linked list.
from typing import List, Optional


# in a min heap, the parent is alway smaller than its children
def sift_up(heap: list[ListNode], index: int):
    parent = (index - 1) // 2
    while index > 0 and heap[parent].val > heap[index].val:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = (index - 1) // 2


def sift_down(heap: list[ListNode], index: int):
    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index
    if left < len(heap) and heap[left].val < heap[smallest].val:
        smallest = left
    if right < len(heap) and heap[right].val < heap[smallest].val:
        smallest = right
    while smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        index = smallest
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(heap) and heap[left].val < heap[smallest].val:
            smallest = left
        if right < len(heap) and heap[right].val < heap[smallest].val:
            smallest = right

def heapprint(heap):
    print([item.val for item in heap])

def heappush(heap: list[ListNode], value: ListNode) -> None:
    heap.append(value)
    sift_up(heap, len(heap) - 1)


def heappop(heap: list[ListNode]) -> ListNode:
    value = heap[0]
    n = len(heap) - 1
    heap[0], heap[n] = heap[n], heap[0]
    heap.pop(n)
    sift_down(heap, 0)
    return value


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for list_node in lists:
            if not list_node:
                continue
            heappush(heap, list_node)
        if not heap:
            return None
        head = heappop(heap)
        current = head
        if current.next:
            heappush(heap, current.next)
        
        # heapprint(heap)
        while heap :
            popped = heappop(heap)
            next_in_heap = popped.next
            if next_in_heap:
                heappush(heap, next_in_heap)
            current.next = popped
            current = popped
        return head


def arr_to_list(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0], None)
    current = head
    for num in arr[1:]:
        next = ListNode(num, None)
        current.next = next
        current = next
    return head


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
output = Solution().mergeKLists([arr_to_list(arr) for arr in lists])
if output:
    output = output.to_arr()
else:
    output = []
expected = [1, 1, 2, 3, 4, 4, 5, 6]
print(f"expected {expected} got {output}")
