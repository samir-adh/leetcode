from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        acc = []
        candidates = sorted(candidates)

        def aux(index: int, subset: List[int], total):
            if total == target:
                acc.append(subset)
                return
            # for i in range(index, len(candidates)):
            #     aux(index + 1, subset + [candidates[index]], total + candidates[index])
            if index >= len(candidates) or total > target:
                return
            aux(index, subset + [candidates[index]], total + candidates[index])
            aux(index + 1, subset, total)

        aux(0, [], 0)
        return acc


def test_case1():
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    output = Solution().combinationSum(candidates, target)
    print(f"expected : {expected}\ngot : {output}")


test_case1()
