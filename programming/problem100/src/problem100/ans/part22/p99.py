M = int(input())
DC = [list(map(int, input().split())) for _ in range(M)]

S = 0
C = 0
for i in range(M):
    d, c = DC[i]
    S += d * c
    C += c

print((C - 1) + (S - 1) // 9)