from collections import deque

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

MOD = 998244353

S = deque([1])
current = 1
power = 1
for q in query:
    if q[0] == 1:
        S.append(q[1])
        current = (current * 10 + q[1]) % MOD
        power = (power * 10) % MOD
    elif q[0] == 2:
        removed = S.popleft()
        power = pow(10, len(S), MOD)
        current = (current - removed * power) % MOD
    else:
        print(current % MOD)
    