from typing import List
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        def findInsertion(intervals : List[List[int]], key: int, value: int):
            left = 0
            right = len(intervals)
            mid = -1
            prev = 0
            while mid != prev:
                prev = mid
                mid = (left + right) // 2
                if intervals[mid][key] == value:
                    return mid
                if intervals[mid][key] >= value:
                    right = mid
                else:
                    left = mid
            return right

        intervals = sorted(intervals, key=lambda x: x[0])
        s, e = newInterval
        s_index = findInsertion(intervals, 0, s)
        e_index = findInsertion(intervals, 1, e)
        if s_index > 0 and intervals[s_index - 1][1] >= s:
            s_index -= 1
            s = intervals[s_index][0]

        if e_index < len(intervals) and intervals[e_index][0] <= e:
            e = intervals[e_index][1]
            e_index += 1

        return intervals[:s_index] + [[s, e]] + intervals[e_index:]
