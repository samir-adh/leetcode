from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        acc = []
        candidates = sorted(candidates)

        def aux(index: int, subset: List[int],total: int):
            if total == target:
                acc.append(subset)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                aux(i+1, subset + [candidates[i]], total + candidates[i])

        aux(0,[], 0)
        return acc

def test_case1():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    output = Solution().combinationSum2(candidates, target)
    print(f"expected : {expected}\ngot : {output}")


if __name__ == "__main__":
    test_case1()
