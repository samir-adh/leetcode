from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = [nums[0]]
        n = len(nums)
        res = nums[0]
        for i in range(1,n):
            x =  max(out[-1]+ nums[i], nums[i])
            res = max(x,res)
            out.append(
                x
            )
        return res