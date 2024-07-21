N = int(input())
A = list(map(int, input().split()))

cnt = 0
right = 0
for left in range(N):
    if left > right:
        right = left
    while right + 1 < N and A[right] < A[right + 1]:
        right += 1
    cnt += (right - left + 1)

print(cnt)