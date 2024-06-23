def is_prime(N):
    if N == 1:
        return False
    if N == 2:
        return True
    
    i = 2
    while i*i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


A, B, C, D = map(int, input().split())

S = []
for i in range(A, B + 1):
    s = []
    for j in range(C, D + 1):
        s.append(i + j)
    S.append(s)

flg = True
for s in S:
    flg1 = False
    for ss in s:
        flg1 |= is_prime(ss)
    flg &= flg1

if flg:
    print("Aoki")
else:
    print("Takahashi")