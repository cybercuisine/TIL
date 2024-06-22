from typing import List

def check_x(x: int, arr: List[int]) -> bool:
    n = len(arr)
    ABS = 10 ** 4
    MAX = 2 * ABS + 1
    dp = [[False] * (MAX) for _ in range(n + 1)]
    dp[0][ABS] = True
    dp[1][arr[0] + ABS] = True

    for i in range(1, n):
        a = arr[i]
        for j in range(MAX):
            if j - a >= 0 :
                dp[i + 1][j] |= dp[i][j - a]
            if j + a < MAX:
                dp[i + 1][j] |= dp[i][j + a]
    
    return dp[n][x + ABS]

def check_y(y: int, arr: List[int]) -> bool:
    n = len(arr)
    ABS = 10 ** 4
    MAX = 2 * ABS + 1
    dp = [[False] * (MAX) for _ in range(n + 1)]
    dp[0][ABS] = True

    for i in range(n):
        a = arr[i]
        for j in range(MAX):
            if j - a >= 0:
                dp[i + 1][j] |= dp[i][j - a]
            if j + a < MAX:
                dp[i + 1][j] |= dp[i][j + a]
    
    return dp[n][y + ABS]


def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))

    odd = []
    even = []
    for i in range(N):
        if i % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])

    flg = check_x(x, even) and check_y(y, odd)

    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
