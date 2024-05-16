from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
actions = [ list(map(lambda x: int(x) - 1, input().split())) for i in range(M) ]

def get_next(pos, x, y, z):
    state = [(pos // (2 ** i)) % 2 for i in range(N)]
    state[x] = 1 - state[x]
    state[y] = 1 - state[y]
    state[z] = 1 - state[z]
    
    ret = 0
    for i in range(N):
        if state[i] == 1:
            ret += 2 ** i
    return ret

G = [list() for i in range(2**N)]
for i in range(2 ** N):
    for x,y,z in actions:
        nextstate = get_next(i,x,y,z)
        G[i].append(nextstate)

start = 0
for i in range(N):
    if A[i] == 1:
        start += 2 ** i
goal = 2 ** N - 1

dist = [-1] * (2 ** N)
dist[start] = 0
Q = deque()
Q.append(start)

while len(Q) >= 1:
    pos = Q.popleft()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex)

print(dist[goal])