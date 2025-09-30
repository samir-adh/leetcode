from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited: set[tuple[int, int]] = set()
        n = len(grid)
        m = len(grid[0])

        def explore(i:int, j:int) -> int:
            queue = [(i, j)]
            area = 0
            visited.add((i,j))
            while queue:
                x, y = queue.pop()
                area += 1

                u, v = x + 1, y
                if u < n and grid[u][v] == 1 and (u, v) not in visited:
                    queue.append((u, v))
                    visited.add((u, v))

                u, v = x - 1, y
                if u >= 0 and grid[u][v] == 1 and (u, v) not in visited:
                    queue.append((u, v))
                    visited.add((u, v))

                u, v = x, y + 1
                if v < m and grid[u][v] == 1 and (u, v) not in visited:
                    queue.append((u, v))
                    visited.add((u, v))

                u, v = x, y - 1
                if v >= 0 and grid[u][v] == 1 and (u, v) not in visited:
                    queue.append((u, v))
                    visited.add((u, v))

            return area
        
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, explore(i,j))
        return maxArea

def test_case1():    
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    expected = 6
    output = Solution().maxAreaOfIsland(grid)
    print(f"expected {expected}, got {output}")

test_case1()