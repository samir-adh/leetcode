class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        def loop(left: int, right: int):
            pali = ""
            while left >= 0 and right < n and s[left] == s[right]:
                pali = s[left : right + 1]
                left -= 1
                right += 1
            nonlocal longest
            if len(pali) > len(longest):
                longest = pali

        for i in range(n):
            # odd palindrome
            left = i
            right = i
            loop(left, right)

            # even palindrome
            left = i
            right = i + 1
            loop(left, right)
        return longest


s = "aacabdkacaa"
expected = "bab"
output = Solution().longestPalindrome(s)
print(f"expected {expected} got {output}")
