from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = len(nums) -1
        jumpLength = 1
        while current != 0:
            if current < jumpLength:
                return False
            source = current - jumpLength
            if nums[source] >= jumpLength:
                current = source
                jumpLength = 1
            else:
                jumpLength += 1
        return True
