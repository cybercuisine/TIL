from functools import lru_cache

N = int(input())

MOD = 998244353

@lru_cache(maxsize=None)
def rec(n):
    result = 0
    if n <= 1:
        return n
    for i in range(2, 7):
        if n % i == 0:
            result += rec(n // i)
    
    return result * inv5 % MOD


inv5 = pow(5, MOD - 2, MOD)


print(rec(N))