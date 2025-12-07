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


def valuesToTheLeft(array: List[int], target: int) -> int:
    left = 0
    right = len(array)
    mid = 0
    prev = 1
    while prev != mid:
        prev = mid
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid
        else:
            right = mid
    return mid


def splittingValue(nums1: List[int], nums2: List[int], splitSize: int) -> int:
    right = max(nums1[-1], nums2[-1])
    left = min(nums1[0], nums2[0])
    prev = 0
    mid = -1
    while prev != mid:
        prev = mid
        mid = (left + right) // 2
        atLeft = valuesToTheLeft(nums1, mid) + valuesToTheLeft(nums2, mid)
        if atLeft == splitSize:
            return mid
        if atLeft < splitSize:
            left = mid
        else:
            right = mid
    return mid


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n * m == 0:
            if n == 0:
                nums = nums2
            else:
                nums = nums1
            n = len(nums)
            return (nums[n // 2] + nums[(n - 1) // 2]) / 2
        fullSize = n + m
        halfSize = (fullSize) // 2
        a = splittingValue(nums1, nums2, halfSize)
        if fullSize % 2:
            return a
        b = splittingValue(nums1, nums2, (fullSize - 1) // 2)
        print(f"a:{a},b:{b}")
        return (a + b) / 2


nums1 = [2, 2, 4, 4]
nums2 = [2, 2, 2, 4, 4]
output = Solution().findMedianSortedArrays(nums1, nums2)
print(output)
print(sorted(nums1 + nums2))
