from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suff = [1] * n
        prod = [1]*n
        for i in range(0, n-1):
            pre[i+1] = pre[i] * nums[i]
            suff[n-i-2] = suff[n-i-1] * nums[n-i-1]
        for i in range(n):
            prod[i] = pre[i] * suff[i]
        return prod


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    out = Solution().productExceptSelf(nums)
    print(f"got : {out}")
    print(f"expected : {expected}")
