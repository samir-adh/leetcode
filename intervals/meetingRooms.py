"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x: x.start)
        n = len(intervals)
        for i in range(1,n):
            end_previous = intervals[i-1].end
            start_current = intervals[i].start
            if end_previous > start_current:
                return False
        return True