from math import gcd

T = int(input())
tests = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    N, D, K = tests[i]
    a = N // gcd(N, D)
    ans = D * (K - 1) % N + (K - 1) // a
    print(ans % N)