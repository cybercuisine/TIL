N = int(input())
HS = [list(map(int, input().split())) for _ in range(N)]

HS.sort(reverse=True)
left = 0
right = 10 ** 20

while right - 1 > left:
    mid = (left + right) // 2
    flg = True
    tmp = []
    for i in range(N):
        h, s = HS[i]
        tmp.append((mid - h) // s)
    tmp.sort()
    for i in range(N):
        if tmp[i] < i:
            flg = False
    if flg:
        right = mid
    else:
        left = mid

print(right)