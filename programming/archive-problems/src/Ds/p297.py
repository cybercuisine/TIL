A, B = map(int, input().split())

cnt = 0
while A != B and A > 0 and B > 0:
    if A > B:
        f = A // B
        cnt += f
        A %= B
    else:
        f = B // A
        cnt += f
        B %= A
    if A == 0 or B == 0:
        cnt -= 1

print(cnt)