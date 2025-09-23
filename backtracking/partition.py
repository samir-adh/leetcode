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

        def aux(j: int, i: int, parts: list[str]):
            if i >= len(s):
                if i == j:
                    acc.append(parts)
                    return
            else :
                sub = s[j : i + 1]
                if isPalindrome(sub):
                    aux(i + 1, i + 1, parts + [sub])
                aux(j, i + 1, parts)

        aux(0, 0, [])
        return acc


s = "aab"
output = Solution().partition(s)
print(output)
