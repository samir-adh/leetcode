"""
Definition of Interval:
"""
from typing import List
from _heapq import heappush, heapreplace
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x : x.start)
        days_ends = [0]
        for meeting in intervals:
            if meeting.start >= days_ends[0]:
                heapreplace(days_ends,meeting.end)
            else :
                heappush(days_ends, meeting.end)
        return len(days_ends)
