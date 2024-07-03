from collections import deque


def Sliding_Window_Minimum(A, L):
    ans = []
    dq = deque()
    for i, a in enumerate(A):
        while dq and a <= dq[-1][1]:
            dq.pop()
        dq.append([i, a])
        if i >= L - 1:
            ans.append(dq[0][1])
        if dq and dq[0][0] <= i + 1 - L:
            dq.popleft()
    return ans


N, K = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
Q = [0] * N
for i in range(N):
    Q[P[i]] = i

mn_pos = Sliding_Window_Minimum(Q, K)
mx_pos = Sliding_Window_Minimum([-i for i in Q], K)

ans = N
for mn, mx in zip(mn_pos, mx_pos):
    ans = min(ans, -mx - mn)
print(ans)
