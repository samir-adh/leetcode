class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            # Odd case
            left = i
            right = i
            while 0 <= left and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            # Even case
            left = i
            right = i + 1
            while 0 <= left and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res


s = "abc"
expected = 3
output = Solution().countSubstrings(s)
print(f"expected {expected}, got {output}")
