from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        acc = []
        candidates = sorted(candidates)

        def aux(index: int, subset: List[int], total):
            if total == target:
                acc.append(subset)
                return
            if index >= len(candidates) or total > target:
                return
            else:
                aux(index + 1, subset + [candidates[index]], total + candidates[index])
                while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                    index += 1
                aux(index + 1, subset, total)

        aux(0, [], 0)
        return acc


def test_case1():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    output = Solution().combinationSum2(candidates, target)
    print(f"expected : {expected}\ngot : {output}")


if __name__ == "__main__":
    test_case1()
