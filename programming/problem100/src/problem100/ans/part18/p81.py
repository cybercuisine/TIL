N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N)]

IDX = 1000009
S = [0] * IDX
for a, b in E:
    S[a] += 1
    S[b + 1] -= 1

for i in range(1, IDX):
    S[i] += S[i - 1]

ans = 0
for i in range(IDX):
    ans = max(ans, S[i])

print(ans)