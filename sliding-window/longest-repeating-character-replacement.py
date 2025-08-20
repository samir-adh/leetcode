class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        count = {}
        max_freq = 0
        max_length = 0
        while end < len(s):
            c = s[end]
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])
            if end - start + 1 - max_freq > k:
                count[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
            end += 1
        return max_length


def test_1():
    s = "ABAB"
    k = 2
    expected = 4
    output = Solution().characterReplacement(s, k)
    assert output == expected, f"Expected {expected}, got {output}"


def test_2():
    s = "AABABBA"
    k = 1
    expected = 4
    output = Solution().characterReplacement(s, k)
    assert output == expected, f"Expected {expected}, got {output}"
