from typing import List

def findInsertion(intervals : List[List[int]], key : int, value: int):
    left = 0
    right = len(intervals)
    prev = -1
    mid = 0
    while prev != mid:
        prev = mid
        mid = (left+right)//2
        if intervals[mid][key] == value:
            return mid
        if intervals[mid][key] >= value:
            right = mid
        else:
            left = mid
    return right


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        def findStart(key: int, value: int):
            return findInsertion(intervals, key, value)
        s,e = newInterval
        s_index = findStart(0,s)
        e_index = findStart(1,e)
        if s_index > 0 and intervals[s_index-1][1] >= s :
            s_index -= 1
            s = intervals[s_index][0]
        if e_index < len(intervals) and intervals[e_index][0] <= e:
            e = intervals[e_index][1]
            e_index += 1

        intervals = intervals[:s_index] + [[s,e]] + intervals[e_index:]
        return intervals


intervals = [[10,20]]
out = Solution().insert(intervals , [4, 8])
print(out)