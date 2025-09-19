from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIdx = [x for x in enumerate(nums)]
        numsIdx = sorted(numsIdx, key=lambda x: x[1])
        left = 0
        right = len(numsIdx)-1
        while left < right:
            val = numsIdx[left][1] + numsIdx[right][1]
            if val == target:
                return [numsIdx[left][0], numsIdx[right][0]]
            elif val > target:
                right -= 1
            else:
                left += 1

        return []
