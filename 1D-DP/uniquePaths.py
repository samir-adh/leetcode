class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [0 for _ in range((m + 1) * (n + 1))]
        for i in range(m):
            mem[n * i + n - 1] = 1
        for j in range(n):
            mem[n * (m - 1) + j] = 1

        def toidx(i: int, j: int):
            return n * i + j

        for i in range(m - 1)[::-1]:
            for j in range(n - 1)[::-1]:
                mem[toidx(i, j)] = mem[toidx(i, j + 1)] + mem[toidx(i + 1, j)]

        return mem[0]


m = 3
n = 7
expected = 28
output = Solution().uniquePaths(m, n)
print(f"expected {expected}, got {output}")
