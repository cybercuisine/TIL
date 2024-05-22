from itertools import permutations
import math

def distance(x1: int, y1: int, x2: int, y2: int) -> int:
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


N = int(input())
city = [tuple(map(int, input().split())) for _ in range(N)]

arr = [i for i in range(N)]

ans = 0

arr = list(permutations(arr))

for idx in arr:
    x1 = city[idx[0]][0]
    y1 = city[idx[0]][1]
    for i in range(1, N):
        x2 = city[idx[i]][0]
        y2 = city[idx[i]][1]
        ans += distance(x1, y1, x2, y2)
        x1 = x2
        y1 = y2

print(ans/len(arr))