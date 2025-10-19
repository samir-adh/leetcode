from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def aux(nums: List[int]):
            nums_copy = [0] + nums
            res = [0] * 3
            n = len(nums_copy)
            res[:2] = nums_copy[:2]
            for i in range(2, n):
                res[i % 3] = max(res[(i - 1) % 3], res[(i - 2) % 3] + nums_copy[i])
            return res[(n - 1) % 3]

        return max(aux(nums[1:]), aux(nums[: len(nums) - 1]))


nums = [3, 4, 3]
expected = 4
output = Solution().rob(nums)
print(f"expected {expected}, got {output}")
