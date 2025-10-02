from typing import DefaultDict, List, OrderedDict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        table = DefaultDict(list[int])
        for course, pre in prerequisites:
            table[course].append(pre)

        visited = OrderedDict()
        cycle = set()

        def dfs(course: int) -> bool:
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in table[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited[course] = None
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return list(visited.keys())


prerequisites = [[1, 0]]
numCourses = 2
expected = [0, 1]
output = Solution().findOrder(numCourses, prerequisites)
print(f"expected {expected}, got {output}")
