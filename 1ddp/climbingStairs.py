class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * 3
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i % 3] = res[(i - 1) % 3] + res[(i - 2) % 3]
        return res[2]


if __name__ == "__main__":
    n = 3
    expected = 3
    output = Solution().climbStairs(n)
    print(f"expected {expected}, got {output}")
