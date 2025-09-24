from _heapq import heappop
from _heapq import heappush
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i,n in enumerate(nums):
            heappush(heap,n)
            if i >= k:
                heappop(heap)
        return heap[0]
                