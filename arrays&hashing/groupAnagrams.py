from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        table: dict[int, List[str]] = {}
        def idx(c: str):
            return ord(c) - ord('a')
        for string in strs:
            val = 1
            for c in string:
                val *= primes[idx(c)]
            table[val] = table.get(val,[]) + [string]
        return list(table.values())

        

    

def test_case1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    out = Solution().groupAnagrams(strs)
    print(out)
if __name__ == "__main__":
    test_case1()