N = int(input())
H = list(map(int, input().split()))

stack = [[float('inf'), 0]]
ans = []
t = 0

for i, h_i in enumerate(H, 1):
    height = 1 if i > 1 else 0
    while stack[-1][0] <= h_i:
        x, j = stack.pop()
        t += (x - height) * (i - j)
        height = x
    t += (h_i - height) * (i - stack[-1][1]) + 1
    stack.append([h_i, i])
    ans.append(t)

print(*ans)
