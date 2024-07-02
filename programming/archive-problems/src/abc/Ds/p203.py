N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def is_valid(mid):
    S = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[i - 1][j - 1] > mid:
                S[i][j] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            S[i][j] += S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1]

    for i in range(K, N + 1):
        for j in range(K, N + 1):
            count = S[i][j] - S[i - K][j] - S[i][j - K] + S[i - K][j - K]
            if count < (K * K) // 2 + 1:
                return False
    return True

left = 0
right = 10 ** 9 + 1
while left < right:
    mid = (left + right) // 2
    if is_valid(mid):
        left = mid + 1
    else:
        right = mid



print(left)