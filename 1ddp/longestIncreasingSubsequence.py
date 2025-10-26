from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        def aux(i: int) -> int:
            if i == 0:
                return 1
            if i in mem:
                return mem[i]
            result = 1
            for j in range(i)[::-1]:
                if nums[j] < nums[i]:
                    result = max(result, aux(j) + 1)
            mem[i] = result
            return result
        
        result = 1
        for i in range(len(nums))[::-1]:
            result = max(result, aux(i))
        return result
    
nums = [1,3,6,7,9,4,10,5,6]
expected = 6
output = Solution().lengthOfLIS(nums)
print(f'expected {expected}, got {output}')
