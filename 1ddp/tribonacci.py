class Solution:
    def tribonacci(self, n: int) -> int:
        output = [1, 1, 0, 0]  # T2, T1, T0, undefined
        for i in range(3, n):
            output[1:] = output[:3]
            output[0] = sum(output[1:])
        return output[0]