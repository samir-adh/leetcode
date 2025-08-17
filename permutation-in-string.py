DEBUG = True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def charindex(c: str):
            base = ord("a")
            return ord(c) - base

        # initialisation
        keytable = [0] * 26
        for c in s1:
            index = charindex(c)
            keytable[index] += 1

        left = 0
        right = len(s1)
        wintable = [0] * 26
        for c in s2[left:right]:
            index = charindex(c)
            wintable[index] += 1

        matches = sum([keytable[i] == wintable[i] for i in range(26)])
        if matches == 26:
            return True
        while right < len(s2):
            # print(f"key: {s1} window:{s2[left:right]} matches {matches}")
            cl = s2[left]
            cl_index = charindex(cl)
            # we remove cl from the table
            wintable[cl_index] -= 1
            # if cl was present as much in the key as in the window
            if keytable[cl_index] == wintable[cl_index] +1:
                matches -= 1
            # if now cl is present as much in the key and the window we can increase the number of matches
            if keytable[cl_index] == wintable[cl_index]:
                matches += 1
            # we increase left
            left +=1
            
            rl = s2[right]
            rl_index = charindex(rl)
            # if there is currently the right amount of rl we'll lose a match
            if keytable[rl_index] == wintable[rl_index]:
                matches-=1
            wintable[rl_index] += 1
            # if now we have the right amount we can increase the number of matches
            if keytable[rl_index] == wintable[rl_index]:
                matches+=1
            # we increase right
            right += 1
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
