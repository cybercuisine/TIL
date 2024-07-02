MOD = 998244353
n = int(input())

k = 0
tn = n
while tn > 0:
    k += 1
    tn //= 10

t = (10**k) % MOD
inv = pow(t - 1, MOD - 2, MOD)
result = n * (pow(t, n, MOD) - 1) * inv
result %= MOD

print(result)
