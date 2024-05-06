N, A, B = map(int, input().split())

dp = [None] * (N + 1)

for i in range(N + 1):
    if i >= A and dp[i-A] == False:
        dp[i] = True
    elif i >= B and dp[i-B] == False:
        dp[i] = True
    else:
        dp[i] = False

if dp[N]:
    print("First")
else:
    print("Second")