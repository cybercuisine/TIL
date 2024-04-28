N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N - 1

while True:
    mid = (left + right) // 2
    if A[mid] == X:
        print(mid+1)
        break
    elif A[mid] < X:
        left = mid + 1
    else:
        right = mid - 1