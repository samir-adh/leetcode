# ex : [1,2,3], [1,2,4] -> [1,1,2,2,3,4] -> median is (2+2)/2 = 2

# Finding the median of an array  means finding a value that splits it in two equally sized parts.
# This means the problem we are trying to solve is to find which items should be located at the left of the median of the hypothetical merged array resulting from the two.
# We already know how many :
# max_take := l//2 +1 items with l = m+n
# if l is odd than the median is the largest element chosen
# if  l is even it is the mean of the 2 largest elements chosen
# To find which items to take, we'll use binary search to find the number of items to take from the longest array :
# there are a few cases to consider, for example if we take 1 element from 'a' (meaning we have to take 3 from  'b') in our example we have :
# l_part = {'a':[1], 'b':[1,2,4]} and r_part {'a':[2,3],'b':[]}
# we know that it's wrong because r_part['a'][0]<l_part['b'][-1] meaning we should take more elements from 'a'
# conversly, if we take 3 elements from 'a':
# l_part = {'a':[1,2,3], 'b':[1]} and r_part {'a':[],'b':[2,4]}
# we have r_part['b'][0]<l_part['a'][-1] meaning we should take less elements from 'a'
# set 'a' to be the longest array, 'b' the shortest
# our search space will be (max_take-len(b)):max_take-1, max_take - take_from_a <= len(b) => take_from_a >= max_take - len(b)
# v := max_take
#
# max_take = (m+n)//2 + 1; n > m
# max_take >= 2m//2 + 1
# max_take >= m + 1
# max_take > m

from typing import List


def findMedian(nums: List[int]):
    n = len(nums)
    if n % 1:
        return nums[n//2]
    else:
        return ((nums[(n-1)//2] + nums[n//2]))/2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        if m == 0:
            return findMedian(nums1)
        full_size = m + n
        left_size = full_size//2 + 1
        max_take = left_size
        min_take = max_take - m  # min_take is always gt 1
        take1 = 0
        take2 = 0
        while min_take <= max_take:
            take1 = (max_take + min_take)//2
            take2 = left_size - take1
            # take less elements from nums1
            if take2 < m and nums1[take1-1] > nums2[take2]:
                max_take = take1 - 1
            # take more from nums1:
            elif take1 < n and nums2[take2-1] > nums1[take1]:
                min_take = take1 + 1
            else:
                break
        print(f"take1 : {take1}")
        print(f"take2 : {take2}")
        print(f"left_size: {left_size}")
        if full_size % 2:  # full_size is odd
            if take2  == 0:
                return nums1[take1-1]
            elif take1 == 0:
                return nums2[take2-1]
            else :
                return max(nums1[take1-1], nums2[take2-1])
        else:
            candidates = []
            if take1 > 0:
                candidates.append(nums1[take1-1]) 
            if take2 > 0:
                candidates.append(nums2[take2-1])
            if take1-2 >= 0:
                candidates.append(nums1[take1-2])
            if take2-2 >= 0:
                candidates.append(nums2[take2-2])
            print(f"candidates : {candidates}")
            two_largest = sorted(candidates)[-2:]
            return sum(two_largest)/2


# a, b = [-10,-9,-8], [1,2]
a, b = [4], [1,2,3]
output = Solution().findMedianSortedArrays(a, b)
expected = findMedian(sorted(a+b))
print(sorted(a+b))
print(f"got {output} expected {expected}")
