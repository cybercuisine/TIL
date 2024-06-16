from collections import defaultdict
import bisect

H, W, rs, cs = map(int, input().split())
N = int(input())
RC = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
DL = [input().split() for _ in range(Q)]

pos_y = defaultdict(list)
pos_x = defaultdict(list)

for r, c in RC:
    pos_y[r].append(c)
    pos_x[c].append(r)

for r in pos_y:
    pos_y[r].sort()

for c in pos_x:
    pos_x[c].sort()

current = [rs, cs]

for d, l in DL:
    l = int(l)
    if d == 'L':
        wall_index = bisect.bisect_left(pos_y[current[0]], current[1]) - 1
        wall_pos = pos_y[current[0]][wall_index] if wall_index >= 0 else 0
        current[1] = max(current[1] - l, wall_pos + 1)
    elif d == 'R':
        wall_index = bisect.bisect_right(pos_y[current[0]], current[1])
        wall_pos = pos_y[current[0]][wall_index] if wall_index < len(pos_y[current[0]]) else W + 1
        current[1] = min(current[1] + l, wall_pos - 1)
    elif d == 'U':
        wall_index = bisect.bisect_left(pos_x[current[1]], current[0]) - 1
        wall_pos = pos_x[current[1]][wall_index] if wall_index >= 0 else 0
        current[0] = max(current[0] - l, wall_pos + 1)
    elif d == 'D':
        wall_index = bisect.bisect_right(pos_x[current[1]], current[0])
        wall_pos = pos_x[current[1]][wall_index] if wall_index < len(pos_x[current[1]]) else H + 1
        current[0] = min(current[0] + l, wall_pos - 1)
    
    print(current[0], current[1])
