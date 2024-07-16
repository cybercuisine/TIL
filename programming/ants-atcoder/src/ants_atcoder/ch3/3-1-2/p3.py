import math

A, B, C = map(int, input().split())


def func(t):
    return A * t + B * math.sin(C * t * math.pi)


left = 0
right = 400

epsilon = 10 ** (-7)

for i in range(100):
    mid = (left + right) / 2
    if func(mid) > 100:
        right = mid
    else:
        left = mid

print(mid)