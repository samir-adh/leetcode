class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def idx(a: str):
            base = ord('a')
            return ord(a) - base
        table = [0] * 26
        for i in range(len(s)):
            table[idx(s[i])] += 1
            table[idx(t[i])] -= 1
        for i in table:
            if i != 0 :
                return False
        return True