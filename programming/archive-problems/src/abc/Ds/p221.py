N = 200010
ans = [0] * N

n = int(input())
input_data = [list(map(int, input().split())) for i in range(n)]

x = []
for a, b in input_data:
    x.append((a, 1))
    x.append((a + b, -1))

x.sort()

cnt = 0
for i in range(len(x) - 1):
    cnt += x[i][1]
    ans[cnt] += x[i + 1][0] - x[i][0]

for i in range(1, n):
    print(ans[i], end=" ")
print(ans[n])
