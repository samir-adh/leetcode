from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def aux(i: int)-> bool:
            if i == 0:
                return True
            if i in mem:
                return mem[i]
            result = False
            for word in wordDict:
                j = i - len(word)
                if j >= 0 and s[j:i] == word:
                    result = result or aux(j)
            mem[i] = result
            return result

        return aux(len(s))

def case2():
    s = "leetcode"
    wordDict = ["leet","code"]
    expected = True
    output = Solution().wordBreak(s, wordDict) 
    print(f"expected {expected}, got {output}")
def case1():
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    expected = False
    output = Solution().wordBreak(s, wordDict) 
    print(f"expected {expected}, got {output}")

case1()