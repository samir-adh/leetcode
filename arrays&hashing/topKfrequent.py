from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table: dict[int, int] = {}
        for n in nums:
            table[n] = table.get(n, 0) + 1
        kvals = [(k, v) for k, v in table.items()]
        c = sorted(kvals, key=lambda x: x[1])[-k:]
        print(c)
        top = [x[0] for x in c]
        return top


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    out = Solution().topKFrequent(nums, k)
    print(out)

