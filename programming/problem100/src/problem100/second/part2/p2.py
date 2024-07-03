N = int(input())
S = list(input())

ans = 0
for i in range(1000):
    tmp = [(i // 100) % 10, (i // 10) % 10, i % 10]
    cnt = 0
    for j in range(N):
        if S[j] == str(tmp[cnt]):
            cnt += 1
        if cnt == 3:
            break
    if cnt == 3:
        ans += 1

print(ans)