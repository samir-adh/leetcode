from typing import List


def largestFarmland(grid: List[List[int]]) -> tuple[int, int]:
    mem = {}
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if i == n - 1 or j == m - 1 or grid[i][j] == 0:
                mem[(i, j)] = grid[i][j]
    directions = [(0, 1), (1, 0), (1, 1)]

    def maxSquareFrom(i: int, j: int) -> int:
        if i >= n or j >= m:
            return 0
        if (i, j) in mem:
            return mem[(i, j)]
        minArea = n + 1
        for di, dj in directions:
            u, v = i + di, j + dj
            minArea = min(minArea, maxSquareFrom(u, v))
        maxArea = 1 + minArea
        mem[(i, j)] = maxArea
        return maxArea

    maxArea = 0
    output = (0, 0)
    outGrid = []
    for i in range(n):
        outGrid.append([])
        for j in range(m):
            area = maxSquareFrom(i, j)
            outGrid[-1].append(area)
            if area > maxArea:
                maxArea = area
                output = (i, j)
    # print(f"max area : {maxArea}")
    # for k in range(len(outGrid)):
    #     print(outGrid[k])
    return output


grid = [
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]
output = largestFarmland(grid)
print(output)
