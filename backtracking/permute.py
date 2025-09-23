from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        acc = []

        def aux(items: List[int], subset: List[int]):
            if len(subset) == len(nums):
                acc.append(subset)
                return
            for i in range(len(items)):
                newItems = items.copy()
                newSubset = subset + [newItems.pop(i)]
                aux(newItems, newSubset)

        aux(nums, [])
        return acc

### With set

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         acc = []

#         def aux(items: set[int], subset: List[int]):
#             if len(subset) == len(nums):
#                 acc.append(subset)
#                 return
#             for i in items:
#                 newItems = items.copy()
#                 newItems.remove(i)
#                 newSubset = subset + [i]
#                 aux(newItems, newSubset)

#         aux(set(nums), [])
#         return acc

def test_case1():
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    output = Solution().permute(nums)
    print(f"expected {expected}\ngot {output}")


if __name__ == "__main__":
    test_case1()
