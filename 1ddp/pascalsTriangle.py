from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Recurence formula : p(r,c) = p(r-1,c-1) + p(r-1,c)
        triangle = [[1]]
        for row in range(1,numRows):
            newRow = []
            n = row+1
            for col in range(n):
                k, l = row-1,col-1
                p_r_c_minus1 = triangle[k][l] if l >= 0 else 0
                p_r_c = triangle[k][l+1] if l < k else 0
                newRow.append(p_r_c + p_r_c_minus1)
            triangle.append(newRow)
        return triangle

numRows = 5
output = Solution().generate(numRows)
print(output)