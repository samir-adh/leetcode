from functools import cache


@cache
def factorial(n: int ) -> int :
    if n <= 1:
        return 1
    return n * factorial(n-1)

def binomial(k:int, n: int) -> int:
    if k < 0 or k > n :
        return 0
    return factorial(n) // (factorial(k)*factorial(n-k))

@cache
def bellNumber(n:int) -> int:
    if n <= 1:
        return 1
    return sum([
        binomial(k,n-1) * bellNumber(k) for k in range(n)
    ])

print(bellNumber(16))