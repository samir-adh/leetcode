from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        current = 0
        nums[-1] = 10000
        n = len(nums)
        while current != (n - 1):
            nextStep = current + 1
            for i in range(current + 1, min(current + nums[current] +1, n)):
                if nextStep + nums[nextStep] < i + nums[i]:
                    nextStep = i
            current = nextStep
            print(f"jump to {current}, range is {current + 1, min(current + nums[current], n)}")
            count += 1
        return count

nums = [2,3,1,1,4]
output = Solution().jump(nums)
print(output)