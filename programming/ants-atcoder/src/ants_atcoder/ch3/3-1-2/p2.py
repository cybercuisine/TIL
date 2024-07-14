R, B = map(int, input().split())
x, y = map(int, input().split())

def can_make_bouquets(mid):
    fr = (R - mid) // (x - 1) if x > 1 else float('inf')
    fb = (B - mid) // (y - 1) if y > 1 else float('inf')

    return fr >= 0 and fb >= 0 and fr + fb >= mid

left = 0
right = 10**19

while right - left > 1:
    mid = (left + right) // 2
    if can_make_bouquets(mid):
        left = mid
    else:
        right = mid

print(left)