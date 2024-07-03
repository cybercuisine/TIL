N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(N):
    ent, _ = AB[i]
    for j in range(N):
        _, ext = AB[j]

        if ent >= ext:
            continue

        cnt = 0
        for k in range(N):
            A, B = AB[k]
            cnt += (ext - ent) + 2 * max(0, (ent - A)) + 2 * max(0, (B - ext))
        ans = min(ans, cnt)

print(ans)