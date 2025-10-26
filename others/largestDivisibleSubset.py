from typing import DefaultDict, List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        graph = DefaultDict(list[int])
        roots = set(nums)
        for i, node in enumerate(nums):
            for nei in nums[i + 1 :]:
                if node % nei == 0:
                    graph[node].append(nei)
                    roots.discard(nei)
        mem = {}

        def dfs(node: int):
            if node in mem:
                return mem[node]
            if len(graph[node]) == 0:
                return [node]
            else:
                longest = [node]
                for nei in graph[node]:
                    traversal = dfs(nei) + [node]
                    if len(traversal) > len(longest):
                        longest = traversal
                mem[node] = longest
                return longest

        longest = []
        for root in roots:
            traversal = dfs(root)
            if len(traversal) > len(longest):
                longest = traversal

        return longest


nums = [1, 2, 3, 4, 8]
expected = [1, 3]
output = Solution().largestDivisibleSubset(nums)
print(f"expected {expected}, got {output}")
