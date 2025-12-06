from typing import List


class Group:

    def __init__(self, value: int, start: int) -> None:
        self.value = value
        self.start = start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        netCost = [g-c for g, c in zip(gas, cost)]
        total = 0
        start = 0
        for i,price in enumerate(netCost):
            total += price
            if total < 0:
                total = 0
                start = i +1
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