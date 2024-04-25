from typing import List

N = int(input())
A = list(map(int, input().split()))

def judge(A: List[int], N: int):
    A.sort()
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] + A[j] > 1000:
                break
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] == 1000:
                    return True
    return False

print("Yes" if judge(A, N) else "No")