from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table: dict[str, int] = {}
        for t in tasks:
            table[t] = table.get(t, 0) + 1
        available = [-execcount for execcount in table.values()]
        heapify(available)
        unvavailble = []
        time = 0
        while available or unvavailble:
            while unvavailble and unvavailble[0][1] <= time:
                execcount, _ = unvavailble.pop(0)
                heappush(available, execcount)
            if available:
                execcount = heappop(available) + 1
                if execcount < 0:
                    unvavailble.append((execcount, time + n + 1))
                time += 1
            else:
                time = unvavailble[0][1]
        return time


def test_case1():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    expected = 8
    out = Solution().leastInterval(tasks, n)
    print(f"expected {expected}; got {out}")


def test_case2():
    tasks = ["A", "B", "A"]
    n = 2
    expected = 4
    out = Solution().leastInterval(tasks, n)
    print(f"expected {expected}; got {out}")


if __name__ == "__main__":
    test_case2()
