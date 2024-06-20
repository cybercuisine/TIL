from itertools import count


def calc(N):
    for i2 in (i * i for i in count(2)):
        if i2 > N:
            break
        while N % i2 == 0:
            N //= i2
    return N

N = int(input())
ans = 0
for i in range(1, N + 1):
    odd = calc(i)
    for j in range(1, N + 1):
        if odd * j * j > N:
            break
        ans += 1
print(ans)