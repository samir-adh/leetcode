from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for i in nums:
            if i in table:
                return True
            else:
                table.add(i)
        return False