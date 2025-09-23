from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        acc = []
        n = len(nums)

        def aux(available : List[int], subset: List[int]):
            if len(subset) == n:
                acc.append(subset)
                return
            for i in range(len(available)):
                item = available.pop(0)
                aux(available, subset + [item])
                available.append(item)
        
        aux(nums, [])
        return acc
                

def test_case1():
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    output = Solution().permute(nums)
    print(f"expected {expected}\ngot {output}")


if __name__ == "__main__":
    test_case1()
