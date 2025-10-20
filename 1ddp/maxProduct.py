from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = -11
        prev = 1
        post = 1
        for i in range(n):
            if prev == 0:
                prev = 1
            p = nums[i] * prev
            prev =p 
            if post == 0:
                post = 1
            q = nums[n-1-i] * post
            result = max(result,p, q)
            post = q
        return result


def case1():
    nums = [2,3,-2,4]
    expected = 6
    output = Solution().maxProduct(nums)
    print(f"expected {expected}, got {output}")


if __name__ == "__main__":
    case1()
