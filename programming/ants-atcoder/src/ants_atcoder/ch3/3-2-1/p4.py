from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

S = list(accumulate(A))


def calc_sum(left, right):
    return S[right] - (S[left - 1] if left - 1 >= 0 else 0)


cnt = 0
right = 0
xor = 0
for left in range(N):
    right = max(left, right)
    while right < N and calc_sum(left, right) == xor ^ A[right]:
        xor ^= A[right]
        right += 1
    cnt += right - left
    xor ^= A[left]

print(cnt)
