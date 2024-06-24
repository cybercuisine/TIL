from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))

S = SortedList(P[:(K - 1)])

for i in range(K - 1, N):
    S.add(P[i])
    print(S[len(S) - K])