from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0,0]
        for n in nums:
            tmp = max(rob[0] + n, rob[1])
            rob[0] = rob[1]
            rob[1] = tmp
        return rob[1]
    


nums = [2, 1, 1, 2]
expected = 4
output = Solution().rob(nums)
print(f"expected {expected}, got {output}")
