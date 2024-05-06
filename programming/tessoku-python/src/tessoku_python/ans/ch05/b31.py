N = int(input())

A3 = N // 3
A5 = N // 5
A7 = N // 7

A15 = N // 15
A21 = N // 21
A35 = N // 35
A105 = N // 105

print(A3 + A5 + A7 - A15 - A21 - A35 + A105)