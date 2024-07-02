from math import factorial


def nCr(n, r):
    numerator = factorial(n)
    denominator = factorial(n - r) * factorial(r)
    return numerator // denominator


A, B, K = map(int, input().split())

ans = ""

num = 1

while 0 < A or 0 < B:
    if A == 0:
        ans += "b"
        B -= 1
        continue

    if B == 0:
        ans += "a"
        A -= 1
        continue

    b_start = num + nCr(A - 1 + B, B)

    if K < b_start:
        ans += "a"
        A -= 1
    else:
        ans += "b"
        num = b_start
        B -= 1

print(ans)
