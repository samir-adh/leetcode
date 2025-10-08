class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        substrings = []
        for i in range(n):
            for j in range(i, n):
                substrings.append(s[i : j + 1])
        return substrings


s = "babad"
expected = "bab"
output = Solution().longestPalindrome(s)
print(f"expected {expected} got {output}")
