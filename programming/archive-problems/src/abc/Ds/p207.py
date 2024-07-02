import sys
import math

sys.setrecursionlimit(10 ** 6) 

INF = 2 ** 63 - 1

N = int(input())

if N == 1:
    print("Yes")
    exit()

S = []
for _ in range(N):
    x, y = map(int, input().split())
    S.append((x,y))

T = []
for _ in range(N):
    x, y = map(int, input().split())
    T.append((x,y))


def get_jyuushin(P_LIST):
    x = 0
    y = 0
    for p in P_LIST:
        x += p[0]
        y += p[1]

    x /= N
    y /= N
    return (x, y)

S_JYUUSHIN = get_jyuushin(S)
T_JYUUSHIN = get_jyuushin(T)


for i in range(N):
    S[i] = (S[i][0] - S_JYUUSHIN[0], S[i][1] - S_JYUUSHIN[1])
    T[i] = (T[i][0] - T_JYUUSHIN[0], T[i][1] - T_JYUUSHIN[1])



z = 0
for i in range(N):
    if S[i][0] == 0 and S[i][1] == 0:
        continue
    z = i
    break


for i in range(N):
    angle = math.atan2(T[i][1], T[i][0]) - math.atan2(S[z][1], S[z][0])

    count = 0
    for j in range(N):
        x2 = S[j][0] * math.cos(angle) - S[j][1] * math.sin(angle)
        y2 = S[j][0] * math.sin(angle) + S[j][1] * math.cos(angle)

        icchi = False
        DICT_MIN = 1e-6 

        for k in range(N):
            dx = abs(T[k][0] - x2)
            dy = abs(T[k][1] - y2)
            if dx <= DICT_MIN and dy <= DICT_MIN:
                icchi = True
                break

        if icchi is False:
            break
        else:
            count += 1

    if count >= N:
        print("Yes")
        exit()

print("No")