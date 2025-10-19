class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def idx(c: str):
            return ord(c) - ord("a")

        table1 = [0] * 26
        for c in s1:
            table1[idx(c)] += 1
        table2 = [0] * 26
        n = len(s1)
        for c in s2[:n]:
            table2[idx(c)] += 1
        errors = 0
        for i in range(26):
            if table1[i] != table2[i]:
                errors += 1
        for i in range(n, len(s2)):
            print(f"Errors : {errors}")
            if errors == 0:
                return True
            # remove first char of the substring
            j = idx(s2[i - n])
            if table2[j] == table1[j]:
                errors += 1
            table2[j] -= 1
            if table2[j] == table1[j]:
                errors -= 1

            # add new char to the substring
            k = idx(s2[i])
            if table2[k] == table1[k]:
                errors += 1
            table2[k] += 1
            if table2[k] == table1[k]:
                errors -= 1

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


def test_4():
    s1 = "adc"
    s2 = "dcda"
    expected = True
    result = Solution().checkInclusion(s1, s2)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_4()
