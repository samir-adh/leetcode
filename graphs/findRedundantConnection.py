from typing import DefaultDict, List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        graph = DefaultDict(list[int])

        def dfs(node: int) -> bool:
            if node in visited:
                return True
            if node in cycle:
                return False
            cycle.add(node)
            for nei in graph[node]:
                # if node == nei:
                # continue
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visited.add(node)
            return True

        result = []
        for a, b in edges:
            visited = set()
            graph[a].append(b)
            graph[b].append(a)
            if not dfs(a):
                result.append([a, b])
        return result


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
output = Solution().findRedundantConnection(edges)
expected = [1, 4]
print(f"expected {expected}, got {output}")
