from bisect import bisect_left

def LIS_with_pairs(L):
    L.sort(key=lambda x: (x[0], -x[1]))
    
    seq = []
    for _, h in L:
        pos = bisect_left(seq, h)
        if len(seq) <= pos:
            seq.append(h)
        else:
            seq[pos] = h
    return len(seq)


N = int(input())
WH = [list(map(int, input().split())) for _ in range(N)]

print(LIS_with_pairs(WH))
