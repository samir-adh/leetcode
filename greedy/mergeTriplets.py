# current = [0,0,0]
# triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [2,3,5]
# take all triplets such that a <= x, b <= y AND c <= z and put them in 'validTriplets'
# validTriplets = [[2,1,4], [2,3,4] , [1,2,5]]
# current =
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def fuse(t1: List[int], t2: List[int]) -> List[int]:
            fused = [max(x, y) for x, y in zip(t1, t2)]
            return fused
        x, y, z = target
        u,v,w = False, False,False
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                u = u or a==x
                v = v or b==y
                w = w or c == z
                if u and v and w:
                    return True
        return u and v and w

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]

output = Solution().mergeTriplets(triplets, target)
print(output)