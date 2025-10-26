def nonDivisibleSubset(k, s):
    # Write your code here
    table = {rem: 0 for rem in range(k)}
    for num in s:
        table[num % k] += 1
    result = min(1, table[0])
    for rem in range(1, k // 2 + 1):
        if 2 * rem == k:
            result += min(1, table[rem])
        else:
            result += max(table[rem], table[k - rem])
    return result


nums = [i + 1 for i in range(10)]
k = 4
expected = 5
output = nonDivisibleSubset(k, nums)
print(f"expected {expected}, got {output}")
