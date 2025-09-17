from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates = sorted(candidates)

        def aux(index: int, subset: List[int], total):
            if total == target:
                output.append(subset)
                return
            for j in range(index, len(candidates)):
                a = candidates[j]
                if total + a > target:
                    return  # because the array is sorted in increasing order
                aux(j, subset + [a], total + a)

        aux(0, [], 0)
        return output


def test_case1():
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    output = Solution().combinationSum(candidates, target)
    output = [sorted(o) for o in output]
    for o in output:
        if o not in expected:
            print(f"wrong subset : '{o}' not found in '{expected}'")
    for e in expected:
        if e not in output:
            print(f"missing subset : '{e}' not found in '{output}'")


if __name__ == "__main__":
    test_case1()
