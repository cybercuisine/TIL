from itertools import product

def case1(N, W, VW):
    VW1 = VW[:(N // 2)]
    VW2 = VW[(N // 2):]

    V1 = []
    for bits in product([0, 1], repeat=len(VW1)):
        ch = [0, 0]
        for i in range(len(bits)):
            bit = bits[i]
            if bit == 1:
                ch[0] += VW1[i][0]
                ch[1] += VW1[i][1]
        if ch[1] <= W:
            V1.append(ch)
    
    V2 = []
    for bits in product([0, 1], repeat=len(VW2)):
        ch = [0, 0]
        for i in range(len(bits)):
            bit = bits[i]
            if bit == 1:
                ch[0] += VW2[i][0]
                ch[1] += VW2[i][1]
        if ch[1] <= W:
            V2.append(ch)
    
    V1.sort(key=lambda x: x[1])
    V2.sort(key=lambda x: x[1])

    max_v2 = [0] * (len(V2) + 1)
    for i in range(1, len(V2) + 1):
        max_v2[i] = max(max_v2[i - 1], V2[i - 1][0])

    ans = 0
    for v1, w1 in V1:
        left = 0
        right = len(V2) - 1
        while left <= right:
            mid = (left + right) // 2
            if w1 + V2[mid][1] <= W:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            ans = max(ans, v1 + max_v2[right + 1])

    print(ans)

def case2(N, W, VW):
    dp = [0] * (W + 1)
    for i in range(N):
        v, w = VW[i]
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    print(max(dp))

def case3(N, W, VW):
    max_v = sum(v for v, w in VW)
    dp = [float('inf')] * (max_v + 1)
    dp[0] = 0
    
    for i in range(N):
        v, w = VW[i]
        for j in range(max_v, v - 1, -1):
            dp[j] = min(dp[j], dp[j - v] + w)
    
    ans = 0
    for i in range(max_v + 1):
        if dp[i] <= W:
            ans = i
    print(ans)

N, W = map(int, input().split())
VW = [list(map(int, input().split())) for _ in range(N)]

min_w = 10 ** 10
for v, w in VW:
    min_w = min(min_w, w)

if N <= 30:
    case1(N, W, VW)
elif min_w <= 1000 and W <= 10 ** 5:
    case2(N, W, VW)
else:
    case3(N, W, VW)
