from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue: List[tuple[int, int, int]] = []
        nOranges = 0
        def cond(i: int, j: int) -> bool:
            return (
                0 <= i < n and 0 <= j < m and grid[i][j] == 1 and (i, j) not in visited
            )

        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    nOranges += 1
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        maxDepth = 0
        while queue:
            i, j, depth = queue.pop(0)

            u, v = i + 1, j
            if cond(u, v):
                queue.append((u, v, depth + 1))
                maxDepth = max(maxDepth, depth + 1)
                visited.add((u, v))

            u, v = i - 1, j
            if cond(u, v):
                queue.append((u, v, depth + 1))
                maxDepth = max(maxDepth, depth + 1)
                visited.add((u, v))

            u, v = i, j + 1
            if cond(u, v):
                queue.append((u, v, depth + 1))
                maxDepth = max(maxDepth, depth + 1)
                visited.add((u, v))

            u, v = i, j - 1
            if cond(u, v):
                queue.append((u, v, depth + 1))
                maxDepth = max(maxDepth, depth + 1)
                visited.add((u, v))
        if len(visited) < nOranges:
            return -1
        return maxDepth

grid = [[2,1,1],[1,1,1],[0,1,2]]
expected = 2
output = Solution().orangesRotting(grid)

print(f"expected {expected}, got {output}")