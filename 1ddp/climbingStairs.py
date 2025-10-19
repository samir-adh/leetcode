class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2, 0]
        for i in range(2, n):
            res[i % 3] = res[(i - 1) % 3] + res[(i - 2) % 3]
        return res[(n - 1) % 3]


if __name__ == "__main__":
    n = 3
    expected = 3
    output = Solution().climbStairs(n)
    print(f"expected {expected}, got {output}")
