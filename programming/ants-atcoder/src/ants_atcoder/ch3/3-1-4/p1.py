N, K = map(int, input().split())
WP = [list(map(int, input().split())) for _ in range(N)]

left = 0.0
right = 100.0
eps = 1e-7  # 精度を高めるための小数点以下の閾値

while right - left > eps:
    mid = (left + right) / 2

    F = []
    for w, p in WP:
        F.append(w * (p - mid))

    F.sort(reverse=True)
    cnt = sum(F[:K])
    
    if cnt >= 0:
        left = mid
    else:
        right = mid

print(left)
