N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for i in range(Q)]

T = list(map(lambda c: ord(c) - ord('a') + 1, S))

MOD = 2147483647
power100 = [None] * (N + 1)
power100[0] = 1
for i in range(N):
    power100[i + 1] = power100[i] * 100 % MOD

H = [None] * (N + 1)
H[0] = 0
for i in range(N):
    H[i + 1] = (H[i] * 100 + T[i]) % MOD

def hash_value(l, r):
    return (H[r] - H[l-1] * power100[r - l + 1]) % MOD

for a,b,c,d in queries:
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")