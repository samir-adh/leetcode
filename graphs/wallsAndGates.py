from typing import List
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)] # up, down, left, right
        
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        visited = set()
        def isValid(a,b):
            return 0 <= a < n and 0 <= b < m and (a,b) not in visited and grid[a][b] > 0 
        while queue:
            i,j,distance = queue.pop(0)
            if grid[i][j] < distance:
                continue
            grid[i][j] = distance
            visited.add((i,j))
            for dx,dy in directions:
                u,v = i+dx, j + dy
                if isValid(u,v):
                    queue.append((u,v, distance + 1))
    

grid =  [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Solution().islandsAndTreasure(grid)
for r in grid:
    print(r)