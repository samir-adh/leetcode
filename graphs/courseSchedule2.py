from typing import DefaultDict, List, OrderedDict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for course in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        indegrees = [0 for course in range(numCourses)]
        for course in range(numCourses):
            for next in graph[course]:
                indegrees[next] += 1

        queue = []
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        traversal = []
        while queue:
            current = queue.pop(0)
            traversal.append(current)
            for nei in graph[current]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        if len(traversal) != numCourses:
            traversal = []
        return traversal


prerequisites = [[1, 0]]
numCourses = 2
expected = [0, 1]
output = Solution().findOrder(numCourses, prerequisites)
print(f"expected {expected}, got {output}")
