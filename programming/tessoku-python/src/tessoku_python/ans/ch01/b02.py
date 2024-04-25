ab = list(map(int, input().split()))

def judge(a: int, b: int):
    for i in range(a, b+1):
        if 100 % i == 0:
            return True
    return False

print("Yes" if judge(ab[0],ab[1]) else "No")