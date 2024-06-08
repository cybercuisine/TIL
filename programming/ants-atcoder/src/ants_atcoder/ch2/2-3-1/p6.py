D = int(input())
n = input()

MOD = 1000000007

dp = [[[0 for k in range(D)] for j in range(2)] for i in range(len(n)+1)]
dp[len(n)][0][0] = 1
dp[len(n)][1][0] = 1

for i in range(len(n)-1, -1, -1):
    for j in range(2):
        for k in range(D):
            if j == 1:
                for d in range(0, 9+1):
                    dp[i][j][k] += dp[i+1][1][(k+d)%D]
                    dp[i][j][k] %= MOD
            else:
                dp[i][j][k] += dp[i+1][0][(k+int(n[i]))%D]
                for d in range(0, int(n[i])):
                    dp[i][j][k] += dp[i+1][1][(k+d)%D]
                    dp[i][j][k] %= MOD
print(int(dp[0][0][0]-1))