N = int(input())

MOD = 998244353


def rec(n):
    global memo

    if n > N:
        return 0
    if n == N:
        return 1
    if n in memo:
        return memo[n]
    
    result = 0
    for i in range(2, 7):
        result += rec(i * n)
    
    result *= inv5
    result %= MOD
    memo[n] = result

    return result


inv5 = pow(5, MOD - 2, MOD)
memo = {}

print(rec(1))