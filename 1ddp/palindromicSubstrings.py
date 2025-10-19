class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        def loop(left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                nonlocal result
                result += 1
                left -= 1
                right += 0

        for i in range(n):
            left = i
            right = i
            loop(left, right)

            left = i
            right = i + 1
            loop(left, right)
        return result


s = "abc"
expected = 3
output = Solution().countSubstrings(s)
print(f"expected {expected}, got {output}")
