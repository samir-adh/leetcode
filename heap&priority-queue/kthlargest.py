from _heapq import heappush
from _heapq import heappop
from _heapq import heapify
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.capacity = k
        heapify(self.heap) 
        while len(self.heap) > self.capacity:
            heappop(self.heap)
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.capacity:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def test_case1():
    commands = zip(["KthLargest", "add", "add", "add", "add", "add"],
                   [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]])
    parse_testcase(commands)


def test_case2():
    commands = zip(
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[1, []], [-3], [-2], [-4], [0], [4]]
    )
    parse_testcase(commands)


def test_case3():
    commands = zip(
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[2, [0]], [-1], [1], [-2], [-4], [3]]
    )
    parse_testcase(commands)


def parse_testcase(commands):

    s = KthLargest(0, [])
    for c, a in commands:
        if c == "KthLargest":
            s = KthLargest(a[0], a[1])  # type: ignore
            print(f"storage : {s}")
        if c == 'add':
            out = s.add(a[0])  # type: ignore
            print(f"storage : {s}, output : {out}")


if __name__ == '__main__':
    test_case3()
