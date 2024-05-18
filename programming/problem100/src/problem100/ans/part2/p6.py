N = int(input())
S = list(input())


ans = 0
for i in range(1000):
    cnt = 0
    temp = [i % 10, (i // 10) % 10, (i // 100) % 10]
    for i in range(N):
        if S[i] == str(temp[cnt]):
            cnt += 1
        if cnt == 3:
            break
    if cnt == 3:
        ans += 1

print(ans)