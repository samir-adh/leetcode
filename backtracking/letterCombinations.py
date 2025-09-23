from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        # print(table)
        acc = []
        if not digits:
            return acc
        def aux(i: int, s: str):
            if i >= len(digits):
                acc.append(s)
                return
            for l in table[int(digits[i])-2]:
                aux(i+1, s + l)
        aux(0,"")
        return acc


output = Solution().letterCombinations("23")
print( output)