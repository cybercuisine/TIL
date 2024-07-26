class LazySegmentTreeMax:
    def __init__(self, len_array):
        left = len_array
        while left != left & -left:
            left += left & -left
        self.num_leaf = left
        self.tree = [0] * (2 * self.num_leaf)
        self.lazy = [0] * (2 * self.num_leaf)

    def eval(self, idx):
        if self.lazy[idx] == 0:
            return
        if idx < self.num_leaf:  
            self.lazy[2 * idx] = self.lazy[idx]
            self.lazy[2 * idx + 1] = self.lazy[idx]
        self.tree[idx] = self.lazy[idx]
        self.lazy[idx] = 0

    def query(self, left, right):
        st_r = [(1, 0, self.num_leaf, False)]  
        st_v = []
        while st_r:
            idx, a, b, status = st_r.pop()
            if status:
                tmp1 = st_v.pop()
                tmp2 = st_v.pop()
                st_v.append(max(tmp1, tmp2))
            else:
                self.eval(idx)
                if right <= a or b <= left:
                    st_v.append(0)
                elif left <= a and b <= right:
                    st_v.append(self.tree[idx])
                else:
                    st_r.append((idx, a, b, True))
                    tmpl = (2 * idx, a, (a + b) // 2, False)
                    tmpr = (2 * idx + 1, (a + b) // 2, b, False)
                    st_r.append(tmpl)
                    st_r.append(tmpr)
        return st_v[0]

    def update(self, left, right, x):
        st_r = [(1, 0, self.num_leaf, False)] 
        while st_r:
            idx, a, b, status = st_r.pop()
            if status:
                self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])
            else:
                if left <= a and b <= right: 
                    self.lazy[idx] = x
                    self.eval(idx)
                elif left < b and a < right:
                    st_r.append((idx, a, b, True))
                    tmpl = (2 * idx, a, (a + b) // 2, False)
                    tmpr = (2 * idx + 1, (a + b) // 2, b, False)
                    st_r.append(tmpl)
                    st_r.append(tmpr)


W, N = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(N)]
sg = LazySegmentTreeMax(W + 1)

for left, right in LR:
    m = sg.query(left, right + 1) + 1
    print(m)
    sg.update(left, right + 1, m)