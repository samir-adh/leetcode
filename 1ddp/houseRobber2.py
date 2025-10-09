from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def aux(nums: List[int]):
            if len(nums) < 3:
                return max(nums)

            res = nums[:3]
            res[1] = max(res[:2])
            for i in range(2, len(nums)):
                res[2] = max(res[1], res[0] + nums[i])
                res[:2] = res[1:]
            return res[2]

        return max(aux(nums[1:]), aux(nums[: len(nums) - 1]))


nums = [3, 4, 3]
expected = 4
output = Solution().rob(nums)
print(f"expected {expected}, got {output}")
