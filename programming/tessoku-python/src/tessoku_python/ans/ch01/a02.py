nx = list(map(int, input().split()))
N = nx[0]
X = nx[1]
A = list(map(int, input().split()))

if X in A:
    print("Yes")
else:
    print("No")