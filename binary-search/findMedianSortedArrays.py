# what is the median of two sorted arrays A and B ?
# is is the value x such that |n in A+B, n <=  x| = |n in A+B, n >= x|
# for a single sorted array, its value is:
#       (array[len(array)//2] + array[len(array)+1//2] )/2
# if the the size of A+B = s, let t = (s+1)//2
# we are looking for u,v such that
# | n in A+B, n <= u | = t and | n in A+B, n >= v | = t
# the mean will then be (u+v)/2
# to find u and v we can use binary search :
# left = -10e6, right = 10e6
# prev = -1, mid = 0
#
# example : we need to have 4 values on each size
# A=1,7,7,7,7,7 B=2,3 ->  1,2,3,7,7,7,7,7 -> [1,7,4], [4,7,5],[5,7,6]
# A=1,4,4 ; B=2,3,4 -> 1,2,3,4,4,4
# halfsize = 3
#
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            n, m = m, n
            nums1, nums2 = nums2, nums1
        half = (n + m) // 2
        left = 0
        right = half
        take = (left + right) // 2
        prev = 0
        while prev != take:
            if nums1[min(take, n) - 1] > nums2[half - min(take, n)]:
                left = take
            elif nums2[half - min(take, n) - 1] > nums1[min(take, n)]:
                right = take
            else:
                break
            prev = take
            take = (left + right) // 2
        print(take)
        return (nums1[min(take, n) - 1], nums2[half - min(take, n) - 1])


nums1 = [1, 2]
nums2 = [3]
# 2,2,2,3,4,4,4,4,5,6
output = Solution().findMedianSortedArrays(nums1, nums2)
print(output)
print(sorted(nums1 + nums2))
