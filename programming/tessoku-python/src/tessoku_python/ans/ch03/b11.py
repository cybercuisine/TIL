N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())


X = [None] * Q
for i in range(Q):
    X[i] = int(input())

for x in X:
    left = 0
    right = N - 1
    while left <= right:
        mid =(left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    print(left)
