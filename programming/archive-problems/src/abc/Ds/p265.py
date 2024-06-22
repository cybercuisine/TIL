from itertools import accumulate

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0] + list(accumulate(A))
st = set(S)

for i in range(N + 1):
    p = P + S[i]
    q = P + Q + S[i]
    r = P + Q + R + S[i]
    if p in st and q in st and r in st:
        print("Yes")
        exit()

print("No")