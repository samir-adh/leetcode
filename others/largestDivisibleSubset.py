from typing import DefaultDict, List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        mem = {}

        def largest_sequence(index: int, prev: int):
            if index >= len(nums):
                return []
            if (index, prev) in mem:
                return mem[(index, prev)]
            else:
                largest = largest_sequence(index + 1, prev)
                if nums[index] % prev == 0:
                    new_sequence = [nums[index]] + largest_sequence(
                        index + 1, nums[index]
                    )
                    if len(new_sequence) > len(largest):
                        largest = new_sequence
                mem[(index, prev)] = largest
                return largest

        return largest_sequence(0, 1)


nums = [1, 2, 3, 4, 8]
expected = [1, 3]
output = Solution().largestDivisibleSubset(nums)
print(f"expected {expected}, got {output}")
