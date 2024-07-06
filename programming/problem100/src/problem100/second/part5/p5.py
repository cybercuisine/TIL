P = float(input())

P = float(input())
rlt = 10 ** 18

def f(x):
    return x + P * (2 ** (-x / 1.5))

left, right = 0, P

cnt = 500

while cnt > 0:
    cnt -= 1
    x1, x2 = (2 * left + right) / 3, (left + 2 * right) / 3
    fun1, fun2 = f(x1), f(x2)

    if fun1 > fun2:
        left = x1
        rlt = min(rlt, fun2)
    else:
        right = x2
        rlt = min(rlt, fun1)

print(rlt)