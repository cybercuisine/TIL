N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
    exit()

cnt = 0
time = 1
right = 0
for left in range(N):
    while right < N and time * S[right] <= K:
        time *= S[right]
        right += 1
    cnt = max(cnt, right - left)

    if right == left:
        right += 1
    else:
        time //= S[left]

print(cnt)