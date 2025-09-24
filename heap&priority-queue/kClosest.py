from typing import List
from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.distance = sqrt((x**2) + (y**2))


def swap(heap: List[Point], i: int, j: int):
    heap[i], heap[j] = heap[j], heap[i]


def sift_up(heap: List[Point], i: int):
    parent = (i-1)//2
    while parent >= 0 and heap[parent].distance < heap[i].distance:
        swap(heap, parent, i)
        i = parent
        parent = (i-1)//2


def sift_down(heap: List[Point], i: int):
    l = 2*i + 1
    r = 2*i + 2
    n = len(heap)
    largest = i
    while True:
        if l < n and heap[largest].distance < heap[l].distance:
            largest = l
        if r < n and heap[largest].distance < heap[r].distance:
            largest = r
        if largest == i:
            break
        else:
            swap(heap, i, largest)
            i = largest
            l = 2*i + 1
            r = 2*i + 2


def heappop(heap: List[Point]):
    swap(heap, 0, len(heap)-1)
    val = heap.pop()
    sift_down(heap, 0)
    return val

# def heapify(heap: List[point]):
#     i = len(heap)//2
#     for j in range(0, i)[::-1]:
#         sift_down(heap, j)


def heappush(heap: List[Point], value: Point):
    heap.append(value)
    sift_up(heap, len(heap)-1)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: list[Point] = []
        for i, (x, y) in enumerate(points):
            p = Point(x, y)
            if i < k:
                heappush(heap, p)
            else:
                if p.distance < heap[0].distance:
                    heap[0] = p
                    sift_down(heap, 0)
        return [[p.x, p.y] for p in heap]

if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    Solution().kClosest(points, k)
