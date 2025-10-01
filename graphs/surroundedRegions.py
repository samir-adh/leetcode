from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        n = len(board)
        m = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i: int, j: int):
            if board[i][j] == "X":
                return
            visited.add((i, j))
            for di, dj in directions:
                u, v = i + di, j + dj
                if 0 < u < n - 1 and 0 < v < m - 1 and (u, v) not in visited:
                    dfs(u, v)

        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)
        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n - 1][j] == "O":
                dfs(n - 1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
print(board)
Solution().solve(board)
print(board)
