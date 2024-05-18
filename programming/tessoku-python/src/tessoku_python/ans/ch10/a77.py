N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x: int) -> bool:
    cnt = 0
    last = 0
    for i in range(len(A)):
        if A[i] - last >= x and L - A[i] >= x:
            cnt += 1
            last = A[i]
    return cnt >= K

left = 1
right = 10 ** 9

while left < right:
    mid = (left + right + 1) // 2
    if not check(mid):
        right = mid - 1
    else:
        left = mid

print(left)