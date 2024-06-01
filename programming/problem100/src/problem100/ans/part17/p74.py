MOD = 10**9+7
n = int(input())
k = int(input())
MX = 2 * 10**5
fact = [1] * (MX+1)
factinv = [1] * (MX+1)
for i in range(MX):
    fact[i+1] = fact[i] * (i+1) % MOD
    factinv[i+1] = pow(fact[i+1], MOD-2, MOD)
ans = fact[n+k-1] * factinv[k] * factinv[n-1]
print (ans%MOD)