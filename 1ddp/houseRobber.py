from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        res = [0, 0, 0]
        res[:2] = nums[:2]
        res[1] = max(res[:2])
        for i in range(2, len(nums)):
            res[2] = max(res[1], res[0] + nums[i])
            res[:2] = res[1:]
        return res[2]


nums = [2, 1, 1, 2]
expected = 4
output = Solution().rob(nums)
print(f"expected {expected}, got {output}")
