class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while  left <= right:
            middle = left + (right - left) // 2
            a = nums[middle]
            if a == target:
                return middle
            elif a < target:
                left = middle + 1
            else :
                right = middle -1
        return -1 
    

def test_case1():
    input = [-1,0,3,5,9,12]
    target = 9
    expected = 4
    output = Solution().search(input, target)
    assert expected == output

def test_case2():
    input = [-1,0,3,5,9,12]
    target = 2
    expected = -1
    output = Solution().search(input, target)
    assert expected == output

def test_case3():
    input = [5]
    target = 5
    expected = 0
    output = Solution().search(input, target)
    assert expected == output

if __name__ =="__main__":
    test_case3()
