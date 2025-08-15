DEBUG = True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def cindex(c: str):
            base = ord("a")
            return ord(c) - base

        if len(s1) == 0:
            return True
        if len(s2) < len(s1):
            return False

        s1table = [0] * 26
        start = 0
        end = len(s1)

        for c in s1:
            s1table[cindex(c)] += 1

        wintable = [0] * 26
        for c in s2[:end]:
            wintable[cindex(c)] += 1

        matches = 0
        for i in range(26):
            if s1table[i] == wintable[i]:
                matches += 1

        if matches == 26:
            return True

        while end < len(s2):
            start_index = cindex(s2[start])
            # if there was the same number of this particular char
            wintable[start_index] -= 1
            if wintable[start_index] + 1 == s1table[start_index]:
                matches -= 1
            if wintable[start_index] == s1table[start_index]:
                matches += 1

            start += 1

            end += 1
            end_index = cindex(s2[end - 1])
            wintable[end_index] += 1
            if wintable[end_index] == s1table[end_index]:
                matches += 1
            if wintable[end_index] - 1 == s1table[end_index]:
                matches -= 1

            if matches == 26:
                return True
        return False


def test_1():
    """Test case where s1's permutation exists in s2"""
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True
    result = Solution().checkInclusion(s1, s2)
    assert result == expected, f"Expected {expected}, got {result}"


def test_2():
    s1 = "eidbaooo"
    s2 = "ab"
    expected = False
    result = Solution().checkInclusion(s1, s2)
    assert result == expected, f"Expected {expected}, got {result}"


def test_3():
    s1 = "ab"
    s2 = "eidboaoo"
    expected = False
    result = Solution().checkInclusion(s1, s2)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_1()
