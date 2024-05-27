ans = []
N = 10 ** 6
dp = [ 10 ** 10 ] * (N + 1)
dp_odd = [ 10 ** 10 ] * (N + 1)
dp[0] = 0
dp_odd[0] = 0

for i in range(1, 10 ** 3):
    w = i * (i + 1) * (i + 2) // 6
    if N <= w:
        break
    for n in range(N - w):
        new = dp[n] + 1
        if new < dp[n + w]:
            dp[n + w] = new
    if w & 1 == 1:
        for n in range(N - w):
            new = dp_odd[n] + 1
            if new < dp_odd[n + w]:
                dp_odd[n + w] = new

while True:
    s = int(input())
    if s == 0:
        break
    ans.append([dp[s], dp_odd[s]])

for a, b in ans:
    print(a, b)