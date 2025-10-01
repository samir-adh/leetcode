from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac = set()
        atl = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i: int, j: int, path: set[tuple[int, int]]):
            path.add((i, j))
            for di, dj in directions:
                u, v = i + di, j + dj
                if (
                    0 <= u < n
                    and 0 <= v < m
                    and (u, v) not in path
                    and heights[i][j] <= heights[u][v]
                ):
                    dfs(u, v, path)

        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m - 1, atl)
        for j in range(m):
            dfs(0, j, pac)
            dfs(n - 1, j, atl)

        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i, j])
        return res


def case1():
    grid = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    output = Solution().pacificAtlantic(grid)
    print(f"expected {expected}\ngot {output}")


def case2():
    grid = [
        [1],
    ]
    expected = [[0, 0]]
    output = Solution().pacificAtlantic(grid)
    print(f"expected {expected}\ngot {output}")


case1()
