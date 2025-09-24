from _heapq import heappush
from _heapq import heappop
from _heapq import heapify
from typing import List



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)
            c = -abs(a-b)
            if c < 0:
                heappush(stones, c)
        if not stones:
            return 0
        return -stones[0]
