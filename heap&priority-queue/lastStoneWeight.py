from typing import List


def sift_up(heap: List[int], i: int):
    parent = (i-1)//2
    while parent > 0 and heap[parent] < heap[i]:
        swap(heap, parent, i)
        i = parent
        parent = (i-1)//2


def sift_down(heap: List[int], i: int):
    l = 2*i + 1
    r = 2*i+2
    largest = i
    n = len(heap)
    while True:
        if l < n and heap[largest] < heap[l]:
            largest = l
        if r < n and heap[largest] < heap[r]:
            largest = r
        if largest == i:
            break
        else:
            swap(heap, largest, i)
            i = largest
            l = 2*i + 1
            r = 2*i + 2


def heapify(heap: List[int]):
    n = len(heap)
    i = n//2
    for j in range(0, i)[::-1]:
        sift_down(heap, j)


def heappop(heap: List[int]):
    swap(heap, 0, len(heap)-1)
    val = heap.pop()
    sift_down(heap, 0)
    return val


def heappush(heap: List[int], val: int):
    heap.append(val)
    sift_up(heap, len(heap)-1)


def swap(heap: List[int], i: int, j: int):
    heap[i], heap[j] = heap[j], heap[i]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(stones)
        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)
            c = abs(a-b)
            if c > 0:
                heappush(stones, c)
        if not stones:
            return 0
        return stones[0]
