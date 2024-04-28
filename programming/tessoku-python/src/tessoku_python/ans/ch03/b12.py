N = int(input())

left = 1
right = 100

while True:
    mid = (left + right) / 2
    f = mid**3 + mid
    if abs(f - N) < 0.001:
        print(mid)
        break
    elif f < N:
        left = mid
    else:
        right = mid