from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNodes = set([node for node, neis in enumerate(graph) if len(neis) == 0])
        # print(safeNodes)
        visited = safeNodes.copy()

        def isSafe(node: int) -> bool:
            # print(f"node : {node}, visited : {visited}, safe : {safeNodes}")
            if node in safeNodes:
                return True
            if node in visited:
                return False
            allSafe = True
            visited.add(node)
            for nei in graph[node]:
                allSafe = allSafe and isSafe(nei)
            # visited.remove(node)
            if allSafe:
                safeNodes.add(node)
            return allSafe

        for node in range(len(graph)):
            isSafe(node)
        return list(safeNodes)


def test_case1():
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    output = Solution().eventualSafeNodes(graph)
    print(output)


def test_case2():
    graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    output = Solution().eventualSafeNodes(graph)
    print(output)


test_case1()
test_case2()
