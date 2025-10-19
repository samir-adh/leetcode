from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 1
        post = 1
        maxp = -11
        for i in range(0,n):
            if nums[i] ==  0:
                pre = 1
                maxp= max(0, maxp)
            else :
                pre *= nums[i]
                maxp= max(pre, maxp)

            if nums[n-i-1] ==  0:
                post = 1
                maxp= max(0, maxp)
            else :
                post *= nums[n-i-1]
                maxp= max(post, maxp)
            print(f'pre {pre}, post {post}')
        return maxp

def case1():
    nums = [-2,0,-1]
    expected = 6
    output = Solution().maxProduct(nums)
    print(f"expected {expected}, got {output}")


if __name__ == "__main__":
    case1()
