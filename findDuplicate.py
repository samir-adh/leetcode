class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for x in nums:
            y = abs(x)-1
            if nums[y] < 0:
                return y +1 
            nums[y] *=-1
        return -1

            
        


def test_case1():
    nums = [1, 3, 4, 2, 2]
    expected = 2
    output = Solution().findDuplicate(nums)
    assert expected == output, f"expected {expected}, got {output}"


def test_case2():
    nums = [3,1,3,4,2]
    expected = 3
    output = Solution().findDuplicate(nums)
    assert expected == output, f"expected {expected}, got {output}"


def test_case3():
    nums = [3,3,3,3,3]
    expected = 3
    output = Solution().findDuplicate(nums)
    assert expected == output, f"expected {expected}, got {output}"


if __name__=="__main__":
    test_case2()