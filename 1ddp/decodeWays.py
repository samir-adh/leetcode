class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = [0, 0, 0]
        res[0] = 1
        res[1] = 0 if s[0] == "0" else 1

        for i in range(2, n+1):
            res[2] = 0
            if 0 < int(s[i-1]):
                res[2] += res[1]

            if 9 < int(s[i-2: i]) < 27:
                res[2] += res[0]
            res[:2] = res[1:]
        
        return res[1]


s = "111111111111111111111111111111111111111111111"
# s = "27"
# s = "2101"
# s = "0"

expected = 0
output = Solution().numDecodings(s)
print(f"got {output}")
