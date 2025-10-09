from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        res = [0] * 3
        res[:2] = cost[:2]
        for i in range(2, n):
            res[i % 3] = cost[i] + min(res[(i - 1) % 3], res[(i - 2) % 3])

        return res[(len(cost) - 1) % 3]


def test_case1():
    cost = [10, 15, 20]
    expected = 15
    output = Solution().minCostClimbingStairs(cost)
    print(f"expected {expected}, got {output}")


if __name__ == "__main__":
    test_case1()
