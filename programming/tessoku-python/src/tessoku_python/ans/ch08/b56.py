mod = 2147483647

def get_hash_left(l, r):
    return (H[r] - Power100[r - l + 1] * H[l - 1]) % mod

def get_hash_right(l, r):
    l, r = N + 1 - r, N + 1 - l
    return (HRev[r] - Power100[r - l + 1] * HRev[l - 1]) % mod

N, Q = map(int, input().split())
S = input()
queries = [tuple(map(int, input().split())) for _ in range(Q)]

S = list(S)
for i in range(N):
    S[i] = ord(S[i]) - ord('a') + 1

SRev = S[::-1]

Power100 = [1] * (N + 1)
for i in range(N):
    Power100[i + 1] = Power100[i] * 100 % mod

H = [1] * (N + 1)
for i in range(N):
    H[i + 1] = (H[i] * 100 + S[i]) % mod

HRev = [1] * (N + 1)
for i in range(N):
    HRev[i + 1] = (HRev[i] * 100 + SRev[i]) % mod

for l, r in queries:
    v1 = get_hash_left(l, r)
    v2 = get_hash_right(l, r)
    if v1 == v2:
        print("Yes")
    else:
        print("No")