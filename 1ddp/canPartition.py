from typing import List
# partition the array into two subset such that the sum
# of the first subset equals the sum of the second
# first observation :
# the problem is analogous to:
# find 1 subset of arr such that sum(subset) == sum(arr)/2
# -> note the if sum(arr) is odd this proble have no solution

# solution :
# use a dfs to find a subset -> 2^n complexity
# use dp to remember attainable targets
# issue WE CAN ONLY PICK AN ELEMENT ONCE
#

# solution 2:
# brute force : try every possible sum of element
# maybe build an array of possible sum by iterating over arr
# target = sum(arr)//2
# start with sumset = {0}
# for item in arr
#   new_set = sumset.copy()
#   for subsum in sumset:
#       newsum = subsum + item
#       if newsum == target:
#            return true
#       new_set.add(newsum)
#   return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumnums = sum(nums)
        if (sumnums % 2) == 1:
            return False
        target = sumnums/2
        sumset = set([0])
        for item in nums:
            current_set = sumset.copy()
            for subsum in current_set:
                newsum = subsum + item
                if newsum == target:
                    return True
                sumset.add(newsum)
        return False

nums = [1, 3, 4, 4]
output = Solution().canPartition(nums)
expected = True
print(f"expected {expected}, got : {output}")
