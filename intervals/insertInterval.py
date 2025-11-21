from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        s,e = newInterval
        for i, (i_s,i_e) in enumerate(intervals):
            if e < i_s :
            # we will never be able to insert it anymore so we do it now
                output.append([s,e])
                return output + intervals[i:]
            if s > i_e:
            # then we'll have to insert the interval after
                output.append([i_s,i_e])
            else:
                # that means the start or the end of new interval is in the middle of the current one
                # so we fuse them and try to insert the newly formed interval
                s = min(s, i_s)
                e= max(e, i_e)
        output.append([s,e])
        return output
intervals=[[1,3],[6,9]]
newInterval=[2,5]
out = Solution().insert(intervals , newInterval)
print(out)