N = int(input())

arr = [i for i in range(9, -1, -1)]

for x in arr:
    pow = 2**x
    print((N // pow) % 2, end='')

print()