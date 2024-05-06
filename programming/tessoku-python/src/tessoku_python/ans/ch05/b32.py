N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [None] * (N + 1)

for i in range(N + 1):
    dp[i] = False
    for j in range(K):
        if i >= a[j] and dp[i-a[j]] == False:
            dp[i] = True
    
if dp[N]:
    print("First")
else:
    print("Second")