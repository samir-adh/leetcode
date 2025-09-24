from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word: str):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        acc = []
        n = len(s)

        def aux(i: int, part: list[str]):
            if i >= n:
                acc.append(part)
                return
            for j in range(i, n):
                sub = s[i:j+1]
                if isPalindrome(sub):
                    aux(j+1, part + [sub])
        aux(0, [])
        return acc


s = "aab"
output = Solution().partition(s)
print(output)
