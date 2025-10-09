class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxpali = ""
        for i in range(n):
            # Case odd
            left = i
            right = i
            res = s[left]
            while left >= 0 and right < n and s[left] == s[right]:
                res = s[left : right + 1]
                left -= 1
                right += 1
            if len(res) > len(maxpali):
                maxpali = res
            # Case even
            left = i
            right = i + 1
            res = ""
            while left >= 0 and right < n and s[left] == s[right]:
                res = s[left : right + 1]
                left -= 1
                right += 1
            if len(res) > len(maxpali):
                maxpali = res

        return maxpali


s = "aacabdkacaa"
expected = "bab"
output = Solution().longestPalindrome(s)
print(f"expected {expected} got {output}")
