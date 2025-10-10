from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table: dict[float, float] = {
            **{k: 1 for k in coins},
            **{0: 0}
        }

        def aux(target: int) -> float:
            if target < 0:
                return inf
            if target in table:
                return table[target]
            ncoins = inf
            for coin in coins:
                res = 1 + aux(target - coin)
                ncoins = min(res,ncoins)
            table[target] = ncoins
            return ncoins

        res = aux(amount)
        if res == inf:
            return -1
        else : 
            return int(res)
    

coins = [2]
amount = 3
expected = -1
output = Solution().coinChange(coins, amount)
print(f"expected {expected} got {output}")
