from typing import DefaultDict, List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        eventFlow = DefaultDict(int)
        for s,e in intervals:
            eventFlow[s] += 1
            eventFlow[e] -= 1
        output = []
        keys = sorted(eventFlow.keys())
        start = int(10e5)
        active_events = 0
        for timestamp in keys:
            active_events += eventFlow[timestamp]
            if active_events == 0:
                output.append([min(start,timestamp),timestamp])
                start = int(10e5)
            else:
                start = min(start,timestamp)
        return output
    
intervals = [[0,0] ,[1,3],[2,6],[8,10], [15,18]]
output = Solution().merge(intervals)
print(output)