class Solution:
    def divisorGame(self, n: int) -> bool:
        # u_n+1 = u_n - x with x such as x < n and n % x == 0
        rounds = 0
        divisor = n
        players = ["Alice", "Bob"]
        print(f"Starting with {n}")
        while True:
            rounds += 1
            divisor = 0
            for i in range(n-1,0,-1):
                if n % i == 0:
                    divisor = i
                    break
            if divisor == 0:
                print(f"{players[(rounds-1)%2]} can't play")
                break
            print(f"{players[(rounds-1)%2]} plays {divisor}")
            n -= divisor
        return rounds%2 == 0

output = Solution().divisorGame(4)
print(output)