from itertools import accumulate


N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

S = list(accumulate(A))

for xi in X:
    cnt = 0
    right = 0
    for left in range(N):
        while right < N and (S[right] - (S[left - 1] if left > 0 else 0)) <= xi:
            right += 1
        cnt += (right - left)
    print(cnt)
