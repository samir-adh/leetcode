from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        waysForTarget: list[set[int]] = []
        n = len(nums)
        if sum(nums)%k != 0:
            return False
        mainTarget = sum(nums)//k
        def findWaysToMakeTarget(index: int, subset: set[int], target : int):
            if target < 0:
                return
            if target == 0:
                waysForTarget.append(subset)
                return
            if index >= n:
                return
            findWaysToMakeTarget(index+1, subset.union([index]), target-nums[index])
            findWaysToMakeTarget(index+1, subset, target)
        findWaysToMakeTarget(0, set(), mainTarget)
        print(waysForTarget)
        validSubsets: list[set[int]] = [set()]
        for subset in waysForTarget:
            currentValids = validSubsets.copy()
            for valid in currentValids:
                if len(valid.intersection(subset)) > 0:
                    continue
                newsubset = valid.union(subset)
                if len(newsubset) == n:
                    return True
                validSubsets.append(newsubset)
        return False                


nums =[1,1,2,2,2]
k = 3
output = Solution().canPartitionKSubsets(nums, k)
print(output)