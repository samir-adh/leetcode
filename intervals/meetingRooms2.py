"""
Definition of Interval:
"""
from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timestamps = []
        for interval in intervals:
            timestamps.append((interval.start, 1))
            timestamps.append((interval.end, -1))

        timestamps = sorted(timestamps, key = lambda x : x[0])
        current_number_of_rooms = 0
        max_number_of_rooms = 0
        for i, timestamp in enumerate(timestamps[:len(timestamps)-1]):
            current_number_of_rooms += timestamp[1]
            if timestamps[i+1][0] != timestamp[0]:
                max_number_of_rooms = max(max_number_of_rooms, current_number_of_rooms)
        return max_number_of_rooms
    
intervals=[(0,50),(10,60),(60,110),(70,120),(20,70),(30,80),(40,90),(50,100),(80,130),(90,140),(100,150)]
intervals=[(1,5),(2,6),(3,7),(4,8),(5,9)]
output = Solution().minMeetingRooms([Interval(x,y) for x,y in intervals])
print(output)