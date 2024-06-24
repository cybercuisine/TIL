T = int(input())
AS = [list(map(int, input().split())) for _ in range(T)]

for a, s in AS:
    F = []
    for i in range(61):
        if (a >> i) & 1:
            s -= 2 * (2 ** i)
        else:
            F.append(2 ** i)

    for f in reversed(F):
        if s >= f:
            s -= f

    if s == 0:
        print("Yes")
    else:
        print("No")