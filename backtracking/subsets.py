from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total = []
        def aux(i: int, subset):
            if i == len(nums):
                total.append(subset)
            else:
                aux(i+1, subset+[nums[i]])
                aux(i+1, subset)
        aux(0, [])
        return total
    

def test_case1():
    nums = [1,2,3]
    total = Solution().subsets(nums)
    print(total)


                
            
if __name__=="__main__":
    test_case1()