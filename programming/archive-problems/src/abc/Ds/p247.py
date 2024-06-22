from collections import deque

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

balls = deque([])
for q in query:
    if q[0] == 1:
        balls.append([q[1], q[2]])
    else:
        c = q[1]
        ans = 0
        while c > 0:
            num, cnt = balls.popleft()
            if cnt > c:
                cnt -= c
                ans += num * c
                c = 0
                balls.appendleft([num, cnt])
            else:
                ans += num * cnt
                c -= cnt
        print(ans)