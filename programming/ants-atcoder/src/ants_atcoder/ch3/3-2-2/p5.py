N, K, L = map(int, input().split())
A = list(map(int, input().split()))


def check(x):
    left, right = 0, 0
    ans = 0
    cnt = 0
    while left < N:
        while right < N and cnt < K:
            if A[right] <= x:
                cnt += 1
            right += 1

        if cnt == K:
            ans += N - right + 1
        if left == right:
            right += 1
        else:
            if A[left] <= x:
                cnt -= 1
        left += 1
    return ans >= L


right = 10**9
left = 0

while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
