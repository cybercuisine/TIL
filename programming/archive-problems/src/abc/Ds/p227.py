N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 10 ** 18
while right - left > 1:
    mid = (left + right) // 2
    S = 0
    for a in A:
        S += min(a, mid)
    if S >= K * mid:
        left = mid
    else:
        right = mid
    
print(left)