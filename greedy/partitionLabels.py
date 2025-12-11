# an idea would be to go through the string
# we shuold cut the string when for all letters at the left of the cut
# they dont appear in the right side
# for that we can use 
# - a set of all letters at the left of current (included)
# - a dictionary that count the frequecies of each letter
#    and is  decreased each time we encounter a letter
# - additionnally a variable that checks if sum(freq[letter] for followed letter) = 0 and cut if thats the case and reset followed letters 
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fwd = set()
        frq = {}
        for letter in s:
            frq[letter] = frq.get(letter,0) + 1
        cdwn = 0
        output = []
        curr = 0
        for letter in s:
            curr += 1
            if letter not in fwd: 
                fwd.add(letter)
                cdwn += frq[letter]
            cdwn -=1
            if cdwn == 0:
                output.append(curr)
                curr = 0
        return output


s = "eccbbbbdec"
output = Solution().partitionLabels(s)
print(output)