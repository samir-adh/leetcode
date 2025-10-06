from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0]*2
        nums1 = nums[:len(nums)-1]
        for n in nums1:
            tmp = max(rob[0] + n, rob[1])
            rob[0] = rob[1]
            rob[1] = tmp
        rob1 =  rob[1]
        nums2 = nums[1:]
        rob = [0]*2
        for n in nums2:
            tmp = max(rob[0] + n, rob[1])
            rob[0] = rob[1]
            rob[1] = tmp
        rob2 =  rob[1]
        return max(rob1, rob2)
nums = [3,4,3]
expected = 4
output = Solution().rob(nums)
print(f"expected {expected}, got {output}")


