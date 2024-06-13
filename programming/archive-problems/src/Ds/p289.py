from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

dp = [False] * (10 ** 5 + 1)
dp[0] = True
for a in A:
    dp[a] = True

for b in B:
    dp[b] = False

def in_B(a: int):
    idx = bisect_left(B, a)
    if idx >= len(B):
        return False
    return a == B[idx]


for i in range(1, 10 ** 5 + 1):
    if dp[i]:
        continue
    if in_B(i):
        continue

    for a in A:
        if i - a >= 0 and dp[i - a]:
            dp[i] = True

print("Yes" if dp[X] else "No")