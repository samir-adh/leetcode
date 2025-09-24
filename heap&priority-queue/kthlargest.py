from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.capacity = k
        self._heapify_()
        print(self.heap)
        while len(self) > k:
            self._extractmin_()

    def __getitem__(self, index: int):
        return self.heap[index]

    def __setitem__(self, index: int, value: int):
        self.heap[index] = value

    def _swap_(self, i, j):
        self[i], self[j] = self[j], self[i]

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def _sift_down_(self, i: int):
        l = 2*i+1
        r = 2*i + 2
        smallest = i
        n = len(self)
        while True:
            if l < n and self[smallest] > self[l]:
                smallest = l
            if r < n and self[smallest] > self[r]:
                smallest = r
            if smallest != i:
                self._swap_(smallest, i)
                i = smallest
                l = 2*i+1
                r = 2*i+2
            else:
                break

    def _heapify_(self):
        i = len(self)//2
        for j in range(0, i)[::-1]:
            self._sift_down_(j)

    def pop(self):
        return self.heap.pop()

    def _extractmin_(self):
        self._swap_(0, len(self)-1)
        val = self.pop()
        self._sift_down_(0)
        return val

    def _sift_up_(self, i):
        parent = (i-1)//2
        while parent >= 0 and self[i] < self[parent]:
            self._swap_(i, parent)
            i = parent
            parent = (i-1)//2

    def peek(self):
        return self[0]

    def add(self, val: int) -> int:
        self.heap.append(val)
        self._sift_up_(len(self)-1)
        while len(self) > self.capacity:
            self._extractmin_()
        return self.peek()


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
