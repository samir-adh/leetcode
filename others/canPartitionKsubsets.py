from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
       # the number of possible subsets is at most 65k because len(nums) <= 16
       # so we can generate all subsets that equal target (=sum(nums)/k)
       # the we have a k-tuple for loop to iterate to find dijoint subsets
       # the complexity lies in how many subsets have a sum that equal target
        n = len(nums)
        if sum(nums) % k != 0:
            return False
        waysToTarget = []
        def findWaysToTarget(index, subset, target):
            if target == 0:
                waysToTarget.append(subset)
                return
            if target < 0 or index >= n:
                return
            findWaysToTarget(index +1, subset.union([index]), target - nums[index])
            findWaysToTarget(index + 1, subset, target )
            # for j in range(index,n):
                # findWaysToTarget(j+1, subset.union([j]), target - nums[j])
        target = sum(nums)//k
        findWaysToTarget(0, set(), target)
        # now we have subsets of nums which sum equals target
        # what we can do is to find through all possible unions of theses subsets (2^m with m = len(subsets))
        # if we have a union of length n


        validSets:list[set[int]] = [set()]
        for subset in waysToTarget:
            currentValidSets = validSets.copy()
            for valid in currentValidSets:
                if len(valid.intersection(subset)) > 0:
                    continue
                new_subset = valid.union(subset)
                if len(new_subset) == n:
                    return True
                validSets.append(new_subset)
        return False




# nums =[1,2,2,2,1]
nums = [4,4,4,6,1,2,2,9,4,6]
k = 3
expected = True
output = Solution().canPartitionKSubsets(nums, k)
print(output)