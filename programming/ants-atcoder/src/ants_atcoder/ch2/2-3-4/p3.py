# TODO
h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

dp1 = [[[k-1 for k in range(w)] for _ in range(h)] for _ in range(h)]
dp2 = [[[i-1 for i in range(h)] for _ in range(w)] for _ in range(w)]

for i in range(h):
  ok = [a[i][j] for j in range(w)]
  for k in range(w - 1, -1, -1):
    if k != w - 1 and ok[k] == ok[k+1]:
      dp1[i][i][k] = dp1[i][i][k+1]
    else:
      dp1[i][i][k] = k
  for j in range(i + 1, h):
      for k in range(w):
        if ok[k] != a[j][k]:
          ok[k] = ""
      for k in range(w - 1, -1, -1):
        if ok[k]:
          if k != w - 1 and ok[k] == ok[k+1]:
            dp1[i][j][k] = dp1[i][j][k+1]
          else:
            dp1[i][j][k] = k

for k in range(w):
  ok = [a[i][k] for i in range(h)]
  for i in range(h - 1, -1, -1):
    if i != h-1 and ok[i] == ok[i+1]:
      dp2[k][k][i] = dp2[k][k][i+1]
    else:
      dp2[k][k][i] = i
  for l in range(k + 1,w):
    for i in range(h):
      if ok[i] != a[i][l]:
        ok[i] = ""
    for i in range(h-1, -1, -1):
      if ok[i]:
        if i != h-1 and ok[i] == ok[i+1]:
          dp2[k][l][i] = dp2[k][l][i+1]
        else:
          dp2[k][l][i] = i

for ans in range(17):
  if dp1[0][h-1][0]==w-1:
      exit(print(ans))
  
  for i in range(h):
    for j in range(i, h):
      tmp = dp1[i][j]
      for k in range(w):
        next_c = tmp[k] + 1
        if next_c < w:
          tmp[k] = tmp[next_c]
  
  for k in range(w):
    for l in range(k,w):
      tmp = dp2[k][l]
      for i in range(h):
        next_r = tmp[i] + 1
        if next_r < h:
          tmp[i] = tmp[next_r]
  

  for i in range(h):
    for k in range(w):
      l = k-1
      for j in range(h-1, i-1, -1):
        while l!=w-1 and j <= dp2[k][l+1][i]:
          l += 1
        if l > dp1[i][j][k]:
          dp1[i][j][k] = l
  
  for k in range(w):
    for i in range(h):
      j = i-1
      for l in range(w-1, k-1 ,-1):
        while j!=h-1 and l <= dp1[i][j+1][k]:
            j += 1
        if j > dp2[k][l][i]:
            dp2[k][l][i] = j
