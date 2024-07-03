def yakusu(X: int):
    cnt = 0
    i = 1
    while X >= i:
        if X % i == 0:
            cnt += 1
        i += 1
    return cnt


N = int(input())

ans = 0
for i in range(1, N + 1, 2):
    cnt = yakusu(i)
    if cnt == 8:
        ans += 1

print(ans)
