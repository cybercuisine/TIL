N = int(input())

power10 = [10 ** i for i in range(17)]

R = [[None] * 10 for i in range(17)]

for i in range(16):
    digit = (N // power10[i]) % 10
    for j in range(10):
        if j < digit:
            R[i][j] = (N // power10[i + 1] + 1) * power10[i]
        elif j == digit:
            R[i][j] = (N // power10[i + 1]) * power10[i] + (N % power10[i]) + 1
        else:
            R[i][j] = (N // power10[i + 1]) * power10[i]

ans = 0
for i in range(16):
    for j in range(10):
        ans += j * R[i][j]

print(ans)