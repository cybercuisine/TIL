N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))


sum = M * sum(A) + N * sum(C) + B * N * M
print(sum)