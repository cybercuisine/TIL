N = int(input())
balloons = [list(map(int, input().split())) for _ in range(N)]

left = 10 ** 9
right = 0
for h,s in balloons:
    left = min(h, left)
    right = max(right, h + s*N)

def check(x):
    tmp = []
    for i in range(N):
        tmp.append((x - balloons[i][0]) // balloons[i][1])
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

