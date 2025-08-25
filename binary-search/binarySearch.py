class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n*m

        def toidx(k):
            i = k // n
            j = k % n 
            return i,j
        
        while left <= right:
            k = left + (right-left)//2
            i,j = toidx(k)
            if i >= m:
                return False
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = k+1
            else :
                right = k-1
        return False