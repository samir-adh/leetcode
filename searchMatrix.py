class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n * m

        def ktoij(k: int):
            i = k // m
            j = k % m
            return i, j

        while left <= right:
            middle = left + (right - left) // 2
            i, j = ktoij(middle)
            if i >= n:
                return False
            a = matrix[i][j]
            if a == target:
                return True
            elif target > a:
                left = middle + 1
            else:
                right = middle - 1
        return False


def test(nums, target, expected):
    output = Solution().searchMatrix(nums, target)
    assert output == expected


def test_case1():
    nums = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    expected = True
    test(nums, target, expected)


def test_case2():
    nums = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    expected = False
    test(nums, target, expected)


def test_case3():
    nums = [[1]]
    target = 2
    expected = False
    test(nums, target, expected)

def test_case4():
    nums = [[1]]
    target = 1
    expected = True
    test(nums, target, expected)

if __name__ == "__main__":
    test_case4()
