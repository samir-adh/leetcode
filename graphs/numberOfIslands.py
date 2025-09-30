from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited: set[tuple[int, int]] = set()
        n = len(grid)
        m = len(grid[0])

        def explore(i: int, j: int):
            queue = [(i, j)]
            while len(queue) > 0:
                x, y = queue.pop()
                visited.add((x, y))
                if x + 1 < n and grid[x + 1][y] == "1" and (x + 1, y) not in visited:
                    queue.append((x + 1, y))
                if x - 1 >= 0 and grid[x - 1][y] == "1" and (x - 1, y) not in visited:
                    queue.append((x - 1, y))
                if y + 1 < m and grid[x][y + 1] == "1" and (x, y + 1) not in visited:
                    queue.append((x, y + 1))
                if y - 1 >= 0 and grid[x][y - 1] == "1" and (x, y - 1) not in visited:
                    queue.append((x, y - 1))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    explore(i, j)
                    count += 1

        return count


def test_case1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected = 1
    output = Solution().numIslands(grid)
    print(f"expected {expected}, got {output}")

if __name__ == "__main__":
    test_case1()
