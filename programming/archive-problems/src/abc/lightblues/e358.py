def get_fact(n):
    fact = [0] * (n + 1)
    inv = [0] * (n + 1)
    fact[0] = 1
    inv[0] = 1
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = pow(fact[i], -1, mod)
    return fact, inv
def nCk(n, k):
    return fact[n] % mod * inv[k] % mod * inv[n - k] % mod

K = int(input())
C = list(map(int, input().split()))
mod = 998244353
fact, inv = get_fact(K)

dp = [0] * (K + 1)
dp[0] = 1
for i in range(26):
    ndp = [0] * (K + 1)
    for j in range(K + 1):
        for k in range(C[i] + 1):
            if j < k:
                break
            ndp[j] += dp[j - k] * nCk(j, k) % mod
        ndp[j] %= mod
    dp = ndp

ans = 0
for j in range(1, K + 1):
    ans += dp[j]
    ans %= mod
print(ans)