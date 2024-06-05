import math

a, b, x = map(int, input().split())

if x <= b * (a ** 2) / 2:
    tan_theta = (2 * x) / (a * (b ** 2))
    print(90 - math.degrees(math.atan(tan_theta)))
else:
    tan_theta = (2 * b - 2 * x / (a ** 2)) / a
    print(math.degrees(math.atan(tan_theta)))
