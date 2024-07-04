N = int(input())
HS = [list(map(int, input().split())) for _ in range(N)]

left = 10 ** 9
right = 0
for h, s in HS:
    right = max(right, h + s * N)
    left = min(h, left)

def check(x):
    tmp = []
    for i in range(N):
        tmp.append((x - HS[i][0]) // HS[i][1])
    tmp.sort()
    for i in range(N):
        if tmp[i] < i:
            return False
    return True

while right - 1 > left:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)