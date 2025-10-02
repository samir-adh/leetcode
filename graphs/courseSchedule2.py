from typing import DefaultDict, List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        table = DefaultDict(list[int])
        for course, pre in prerequisites:
            table[course].append(pre)

        path = set()
        completed = set()
        schedule = []

        def possible(course: int):
            if course in completed:
                return True
            path.add(course)
            for pre in table[course]:
                if pre in path or not possible(pre):
                    return False
            completed.add(course)
            schedule.append(course)
            path.remove(course)
            table[course] = []
            return True

        for i in range(numCourses):
            if not possible(i):
                return []
        return schedule


prerequisites = [[1, 0]]
numCourses = 2
expected = [0, 1]
output = Solution().findOrder(numCourses, prerequisites)
print(f"expected {expected}, got {output}")
