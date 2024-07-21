N = int(input())
A = list(map(int, input().split()))

S = set()
cnt = 0
right = 0
for left in range(N):
    right = max(left, right)

    while right < N and A[right] not in S:
        S.add(A[right])
        right += 1
    
    cnt = max(cnt, right - left)
    S.remove(A[left])

print(cnt)