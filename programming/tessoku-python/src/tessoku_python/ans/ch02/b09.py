import numpy as np

n = int(input())
COO_list = [list(map(int, input().split())) for _ in range(n)]

delta_paper = np.array([[0] * 1501 for _ in range(1501)])

for a, b, c, d in COO_list:
    delta_paper[b][a] += 1
    delta_paper[b][c] -= 1
    delta_paper[d][a] -= 1
    delta_paper[d][c] += 1

delta_paper = np.cumsum(delta_paper, axis=1)
delta_paper = np.cumsum(delta_paper, axis=0)

print(np.sum(delta_paper > 0))