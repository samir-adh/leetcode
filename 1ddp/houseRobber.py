from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * 3
        nums = [0] + nums
        res[:2] = nums[:2]
        n = len(nums)
        for i in range(2, n):
            res[i % 3] = max(res[(i - 1) % 3], res[(i - 2) % 3] + nums[i])
        return res[(n - 1) % 3]


nums = [2, 1, 1, 2]
expected = 4
output = Solution().rob(nums)
print(f"expected {expected}, got {output}")
