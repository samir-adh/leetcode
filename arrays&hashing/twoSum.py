from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in table:
                return [table[diff], i]
            else:
                table[n] = i