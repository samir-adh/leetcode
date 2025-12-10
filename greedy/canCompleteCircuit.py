from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        end = 1
        n = len(gas)
        if n <= 1:
            return 0
        tank = gas[start] - cost[start]
        while start != end:
            if tank < 0:
                start = (start - 1) % n
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end = (end + 1) % n
        return start



def test_case1():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    expected = 3
    output = Solution().canCompleteCircuit(gas, cost)
    assert expected == output, f'expected {expected}, got {output}'


def test_case2():
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    expected = -1
    output = Solution().canCompleteCircuit(gas, cost)
    assert expected == output, f'expected {expected}, got {output}'


test_case1()