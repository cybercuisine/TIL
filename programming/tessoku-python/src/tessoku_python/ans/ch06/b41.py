X, Y = map(int, input().split())

xy = []

while X > 1 or Y > 1:
    xy.append([X, Y])
    if X > Y:
        X -= Y
    else:
        Y -= X

print(len(xy))
xy.reverse()
for l in xy:
    print(str(l[0]) + " " + str(l[1]))