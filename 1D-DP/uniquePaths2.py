from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        mem = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if obstacleGrid[n - i - 1][m - 1] == 1:
                for k in range(0, n - i):
                    mem[k][m - 1] = 0
                break
            mem[n - i - 1][m - 1] = 1

        for j in range(m):
            if obstacleGrid[n - 1][m - j - 1] == 1:
                for v in range(0, m - j):
                    mem[n - 1][v] = 0
                break
            mem[n - 1][m - j - 1] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[n - i - 1][m - j - 1] == 1:
                    mem[n - i - 1][m - j - 1] = 0
                else:
                    mem[n - i - 1][m - j - 1] = (
                        mem[n - i][m - j - 1] + mem[n - i - 1][m - j]
                    )

        return mem[0][0]


grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
expected = 2
output = Solution().uniquePathsWithObstacles(grid)
print(f"expected {expected}, got {output}")
