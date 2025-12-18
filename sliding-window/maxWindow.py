# i think this can be done in O(nlogn) by sliding the window across the array
# and at each step :
# - remove the unwindowed one
# - add the windowed one
# - check the smallest number in the window
# a trick we could use could be to use a max heap 
# where we store both the number and its index
# so when looking for the min item we can pop it if it's not in the window
# the algo is then:
# slide the window (left:right) and at each step:
# - push the new item  -> (logn) 
# - while heap[0] isn't valid we pop -> this is done at n times it maybe some ve 
# - append heap[0] to result
# and i think this way in amortized complexity we end up on nlogn 
# 0,2,1,4,-1,-2,-3,-4
from typing import List 
from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right = k
        heap = []
        for i in range(k):
            heappush(heap,(-nums[i], i))
        output = []
        while right <= len(nums):
            left = right -k
            num_to_add = nums[right-1]
            heappush(heap, (-num_to_add,right-1))
            while heap[0][1] < left:
                heappop(heap)
            output.append(-heap[0][0])
            right += 1
        return output

def test_case1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [3,3,5,5,6,7]
    output = Solution().maxSlidingWindow(nums, k)
    assert expected == output, f"expected {expected} got {output}"

def test_case2():
    nums = [1,-1]
    k = 1
    expected = [1,-1]
    output = Solution().maxSlidingWindow(nums, k)
    assert expected == output, f"expected {expected} got {output}"
