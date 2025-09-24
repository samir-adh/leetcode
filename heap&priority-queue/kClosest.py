from _heapq import heappop
from _heapq import heappush
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return sqrt(x**2 + y**2)
        plist = [(-dist(x, y), x, y) for (x, y) in points]
        heap = []
        for i, p in enumerate(plist):
            heappush(heap, p)
            if i >= k:
                heappop(heap)
        return [[x, y] for d, x, y in heap]
