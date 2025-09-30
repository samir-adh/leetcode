from typing  import List 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(a:str):
            l = 0
            r = len(a)-1
            while l<r:
                if a[l] != a[r]:
                    return False
                l+=1
                r-=1
            return True
        def aux(index: int, part: List[str]):
            if index >= len(s):
                res.append(part)
                return
            for j in range(index, len(s)):
                sub = s[index: j+1]
                if isPalindrome(sub):
                    aux(j+1, part + [sub])
        aux(0, [])
        return res
    

s = "aab"
out= Solution().partition(s)
print(out)