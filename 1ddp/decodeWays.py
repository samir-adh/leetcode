class Solution:
    def numDecodings(self, s: str) -> int:
        res = [1, 0, 0]
        if s[0] != "0":
            res[1] = 1
            res[2] = 1
        n = len(s)
        for i in range(1, n):
            res[2] = 0
            if s[i] != "0":
                res[2] += res[1]
            if 9 < int(s[i - 1 : i + 1]) < 27:
                res[2] += res[0]
            res[:2] = res[1:]
        return res[2]


s = "111111111111111111111111111111111111111111111"
# s = "27"
# s = "2101"
# s = "0"

expected = 0
output = Solution().numDecodings(s)
print(f"got {output}")
