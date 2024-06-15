def f(k, memo={}):
    if k in memo:
        return memo[k]
    if k == 0:
        return 1
    result = f(k // 2, memo) + f(k // 3, memo)
    memo[k] = result
    return result

N = int(input())
print(f(N))
