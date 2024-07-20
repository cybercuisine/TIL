from itertools import accumulate


class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def add(self, idx, value):
        while idx <= self.size:
            self.tree[idx] += value
            idx += idx & -idx

    def sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(N):
    A[i] -= K

S = [0] + list(accumulate(A))

unique_values = sorted(set(S))
value_to_index = {v: i + 1 for i, v in enumerate(unique_values)}

bit = BIT(len(unique_values))
count = 0

for s in S:
    idx = value_to_index[s]
    count += bit.sum(idx)
    bit.add(idx, 1)

print(count)
