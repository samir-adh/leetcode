from typing import DefaultDict, List


class Solution:
    def canFinish(self, numClasses: int, prerequisites: List[List[int]]):
        graph = {course: [] for course in range(numClasses)}
        for a, b in prerequisites:
            graph[b].append(a)
        indegrees = {}
        for i in range(numClasses):
            indegrees[i] = 0

        for node in range(numClasses):
            for nei in graph[node]:
                indegrees[nei] = indegrees.get(nei, 0) + 1

        queue = []
        for node in graph.keys():
            if indegrees[node] == 0:
                queue.append(node)
        n = 0
        while queue:
            current = queue.pop(0)
            n += 1
            for nei in graph[current]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        return n == numClasses


prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]
numCourses = 100
output = Solution().canFinish(numCourses, prerequisites)
expected = True
print(f"expected {expected} got {output}")
