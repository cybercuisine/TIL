N = int(input())

ans = 0
cnt = 1
while N > 0:
    if (N % 2 == 1):
        ans += cnt
    cnt *= 2
    N //= 10

print(ans)