def is_prime(x: int):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    s = 3
    while x >= s ** 2:
        if x % s == 0:
            return False
        s += 2
    return True

Q = int(input())
LR = [tuple(map(int, input().split())) for _ in range(Q)]

MAX_N = 10 ** 5 + 1
S = [0] * MAX_N
primes = [False] * MAX_N
primes[2] = True
for i in range(3, MAX_N):
    if is_prime(i):
        primes[i] = True
    S[i] = S[i - 1]
    if i % 2 != 0 and primes[i] and primes[(i + 1) // 2]:
        S[i] += 1

ans = []
for l, r in LR:
    ans.append(S[r] - S[l-1])

print(*ans, sep='\n')
