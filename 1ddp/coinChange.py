from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 10**5
        mem = {}
        mem[0] = 0
        for coin in coins:
            mem[coin] = 1

        def aux(target: int) -> int:
            if target < 0:
                return inf
            if target in mem:
                return mem[target]
            mini = inf
            for coin in coins:
                mini = min(mini, aux(target - coin) + 1)
            mem[target] = mini
            return mini

        result = aux(amount)
        if result >= inf:
            return -1
        return result


coins = [186, 419, 83, 408]
amount = 6249
expected = -1
output = Solution().coinChange(coins, amount)
print(f"expected {expected} got {output}")
