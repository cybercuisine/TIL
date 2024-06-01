def solve(graph, V):
    ans = 0
    INF = 10 ** 10
    cost = [[graph[i][j] if i != j else INF for j in range(V)] for i in range(V)]
    for u in range(V):
        for v in range(u + 1, V):
            mn = INF
            for w in range(V):
                mn = min(mn, cost[u][w] + cost[w][v])
            if cost[u][v] > mn:
                print(-1)
                exit()
            elif cost[u][v] < mn:
                ans += cost[u][v]
    return ans
    

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

print(solve(A, N))