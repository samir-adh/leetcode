from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        acc = []
        candidates = sorted(candidates)

        def aux(index: int, subset: List[int], total: int):
            if total == target:
                acc.append(subset)
            elif index >= len(candidates):
                return
            else:
                element = candidates[index]
                if total + element <= target:
                    aux(index + 1, subset + [element], total + element)
                while index < len(candidates) and element == candidates[index]:
                    index += 1
                aux(index, subset, total)
        aux(0, [], 0)
        return acc


def test_case1():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    out = Solution().combinationSum2(candidates, target)
    print(out)


def test_case2():
    candidates = [1, 2]
    target = 4
    out = Solution().combinationSum2(candidates, target)
    print(out)


if __name__ == "__main__":
    test_case1()
    test_case2()
