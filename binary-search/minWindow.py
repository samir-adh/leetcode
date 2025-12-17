from typing import DefaultDict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smallest_window = s + "__"
        counter = DefaultDict(int)
        for char in t:
            counter[char] += 1
        
        errors = len(t)
        left = 0
        right = 0

        while left < len(s) or right < len(s):
            while errors == 0:
                # print(s[left:right])
                if len(smallest_window) > right - left:
                        smallest_window = s[left:right]
                char_to_remove = s[left]
                if char_to_remove in counter:
                    counter[char_to_remove] += 1
                    if counter[char_to_remove] > 0:
                        errors += 1
                left += 1
            right += 1
            if right > len(s):
                break
            char_to_add = s[right-1]
            if char_to_add in counter:
                counter[char_to_add] -= 1
                if counter[char_to_add] >= 0:
                    errors = max(0, errors-1)
        # print(left,right)
        if len(smallest_window) > len(s):
            return ""
        return smallest_window


             


s = "AABAC"
t = "ABD"
expected = "BANC"
output = Solution().minWindow(s, t)
print(f"expected {expected} got {output}")
