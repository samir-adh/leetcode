from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        acc = []

        def isPalindrome(s: str):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def aux(i: int, parts: list[str]):
            if i >= len(s):
                acc.append(parts)
                return
            for j in range(i+1, len(s)+1):
                sub = s[i : j]
                if isPalindrome(sub):
                    aux(j, parts + [sub])
        aux(0, [])
        return acc


s = "aab"
output = Solution().partition(s)
print(output)
