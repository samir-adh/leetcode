from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_all = sum(nums)
        if sum_of_all % 2 == 1:
            return False
        mem = {}
        target = sum_of_all // 2

        def can_obtain_target(index: int, target: int):
            if target < 0:
                return False
            if index == 0:
                return target == 0
            if target in mem:
                if mem[target][0] and index > mem[target][1]:
                    return True
                if not mem[target][0] and index < mem[target][1]:
                    return False
            is_possible = can_obtain_target(index - 1, target) or can_obtain_target(
                index - 1, target - nums[index]
            )
            mem[target] = [is_possible, index]
            return is_possible

        return can_obtain_target(len(nums) - 1, target)


nums = [1, 3, 4, 4]
output = Solution().canPartition(nums)
expected = True
print(f"expected {expected}, got : {output}")
