from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        def pac(i, j):
            return i < 0 or (i < n and j < 0)

        def atl(i, j):
            return (i >= n or j >= n) and not pac(i, j)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        output = set()
        cache = {}

        def inGrid(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i: int, j: int, path: set):
            if (i, j) in cache:
                return cache[(i, j)]
            if not inGrid(i, j):
                p, a = pac(i, j), atl(i, j)
                # print(f"p:{p} a :{a}")
                if p and a:
                    output.add((i, j))
                cache[(i, j)] = (p, a)
                return p, a
            else:
                p, a = False, False
                for di, dj in directions:
                    u = i + di
                    v = j + dj
                    if (u, v) not in path:
                        if inGrid(u, v) and heights[u][v] > heights[i][j]:
                            continue
                        path.add((u, v))
                        dp, da = dfs(u, v, path)
                        path.remove((u, v))
                        p = p or dp
                        a = a or da
                if p and a:
                    # print(f"p:{p} a :{a}")
                    output.add((i, j))
                cache[(i, j)] = (p, a)
                return p, a

        for i in range(n):
            for j in range(m):
                dfs(i, j, set())

        return [[i, j] for i, j in output]


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


case2()
