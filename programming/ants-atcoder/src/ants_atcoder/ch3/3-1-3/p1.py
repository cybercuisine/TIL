N, M = map(int, input().split())
X = [int(input()) for _ in range(M)] + [N + 1] 
 
ok, ng = 2 * 10 ** 9, -1
while abs(ok - ng) > 1:
    T = (ok + ng) // 2
    done = 0
    for i in range(M):
        left_remain = X[i] - done - 1
        if left_remain > T:
            break
 
        done = X[i] + max(max(0, T - 2 * left_remain), (T - left_remain) // 2)
        done = min(done, X[i + 1] - 1)
 
    if done >= N:
        ok = T
    else:
        ng = T
 
print(ok)