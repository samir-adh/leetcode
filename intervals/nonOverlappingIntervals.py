from typing import List


def bsearch(intervals: List[List[int]], value):
    left = 0
    right = len(intervals)
    mid = 0
    prev = -1
    while prev != mid:
        prev = mid
        mid = (left + right)//2
        # if intervals[mid][1] == value:
            # return mid
        if intervals[mid][1] > value:
            right = mid
        else:
            left = mid
    return left


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x :x[1])
        n = len(intervals)
        intervals = [[0,0]] + intervals
        mem = {}
        def scheduleSize(index: int):
            if index == 0:
                return 0
            if index in mem:
                return mem[index]
            else:
                skip = scheduleSize(index - 1)
                latest_end_index = bsearch(intervals, intervals[index][0])
                take = scheduleSize(latest_end_index) + 1
                result = max(skip, take)
                # print(f"skip = {skip}, take = {take}")
                mem[index] = result
                return result
        return n - scheduleSize(n)


intervals = [[1,2],[1,3],[2,3],[3,4]] # n = 5
intervals = [[1,2],[1,2],[1,2]]
# output = bsearch(intervals, 2)
output = Solution().eraseOverlapIntervals(intervals)
print(output)
