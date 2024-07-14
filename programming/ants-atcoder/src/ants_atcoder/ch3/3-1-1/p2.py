import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

left = 0
right = 10 ** 18
while right - 1 > left:
    mid = (right + left) // 2
    cnt = 0
    for a in A:
        cnt += bisect.bisect_right(B, mid // a)
    if cnt >= K:
        right = mid
    else:
        left = mid

print(right)