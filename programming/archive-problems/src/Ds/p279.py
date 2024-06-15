import math


def find_minimum_t(A, B):
    if B == 0:
        return float('inf') if A != 0 else 0

    x_opt = max(0, int((A / (2 * B)) ** (2 / 3)))
    t_opt = A / math.sqrt(1 + x_opt) + B * x_opt

    return t_opt


A, B = map(int, input().split())
t_min = find_minimum_t(A, B)
print(f"{t_min:.7f}")