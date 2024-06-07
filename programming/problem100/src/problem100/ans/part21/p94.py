def cmp(a, b):
    return a[0] * a[1] < b[0] * b[1]

def main():
    ans = []
    while True:
        try:
            N, W, D = map(int, input().split())
            if W == 0:
                break
        except:
            break
        
        res = [(W, D)]
        for _ in range(N):
            p, s = map(int, input().split())
            p -= 1
            cur = res[p]
            res.pop(p)
            ne = [(cur[0], cur[1]), (cur[0], cur[1])]
            s %= (cur[0] + cur[1]) * 2
            if s <= cur[0]:
                ne[0] = (s, cur[1])
                ne[1] = (cur[0] - s, cur[1])
            elif s - cur[0] <= cur[1]:
                ne[0] = (cur[0], s - cur[0])
                ne[1] = (cur[0], cur[1] - ne[0][1])
            elif s - cur[0] - cur[1] <= cur[0]:
                ne[0] = (cur[0] - (s - cur[0] - cur[1]), cur[1])
                ne[1] = (cur[0] - ne[0][0], cur[1])
            else:
                ne[0] = (cur[0], (cur[0] + cur[1]) * 2 - s)
                ne[1] = (cur[0], cur[1] - ne[0][1])
            if ne[0] < ne[1]:
                res.append(ne[0])
                res.append(ne[1])
            else:
                res.append(ne[1])
                res.append(ne[0])
        
        res.sort(key=lambda x: x[0] * x[1])
        ans.append(res)
    for res in ans:
        print(" ".join(str(x[0] * x[1]) for x in res))

if __name__ == "__main__":
    main()
