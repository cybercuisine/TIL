N, D = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]

LR.sort(key=lambda x: x[1])

ans = 0
prev_punch_end = -1 

for left, right in LR:
    if prev_punch_end < left:
        ans += 1
        prev_punch_end = right + D - 1

print(ans)
