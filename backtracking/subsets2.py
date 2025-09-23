from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        acc = []
        nums = sorted(nums)

        def aux(index: int, subset: List[int]):
            if index >= len(nums):
                acc.append(subset)
                return
            aux(index+1, subset + [nums[index]])
            while index +1 < len(nums) and nums[index +1] == nums[index]:
                index += 1
            aux(index +1 , subset)

        aux(0, [])
        return acc


def test_case1():
    nums = [1, 2, 2]
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    output = Solution().subsetsWithDup(nums)
    print(f"expected {expected}\ngot {output}")


if __name__ == "__main__":
    test_case1()
