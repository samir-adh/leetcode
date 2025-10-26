from typing import DefaultDict, List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        graph = DefaultDict(list[int])

        def graph_has_cycle(node, parent):
            if node in cycle:
                return True
            if node in visited:
                return False
            cycle.add(node)
            for nei in graph[node]:
                if nei != parent and graph_has_cycle(nei, node):
                    return True
            cycle.remove(node)
            return False

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            if graph_has_cycle(a, -1):
                return [a, b]
        return []


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
output = Solution().findRedundantConnection(edges)
expected = [1, 4]
print(f"expected {expected}, got {output}")
