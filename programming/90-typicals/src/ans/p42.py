MOD = 10**9 + 7

def count_numbers(K):
    dp = [[0] * 9 for _ in range(K + 1)]
    dp[0][0] = 1
    
    for s in range(K):
        for r in range(9):
            if dp[s][r] > 0:
                for d in range(1, 10):
                    new_s = s + d
                    if new_s <= K:
                        new_r = (r + d) % 9
                        dp[new_s][new_r] = (dp[new_s][new_r] + dp[s][r]) % MOD
    
    return dp[K][0]

K = int(input())
print(count_numbers(K))
