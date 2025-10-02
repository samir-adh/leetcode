from typing import DefaultDict, List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        table = DefaultDict(list[int])
        for course, pre in prerequisites:
            table[pre].append(course)

        visited = set()
        cycle = set()
        path = []

        def dfs(k: int) -> bool:
            if k in cycle:
                return False
            if k in visited:
                return True
            cycle.add(k)
            for c in table[k]:
                if not dfs(c):
                    return False
            cycle.remove(k)
            visited.add(k)
            path.append(k)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return path
