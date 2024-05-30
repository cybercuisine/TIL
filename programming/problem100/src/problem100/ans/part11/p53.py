from bisect import bisect_left

def LIS(L):
    seq = []
    for ai in L:
        pos = bisect_left(seq, ai)
        if len(seq) <= pos:
            seq.append(ai)
        else:
            seq[pos] = ai
    return len(seq)

N = int(input())
A = [int(input()) for _ in range(N)]

print(LIS(A))