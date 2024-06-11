
def input_q(n: int):
    print(f"? {str(n)}", flush=True)
    si = int(input())
    return si

N = int(input())

left = 1
right = N
mid = (left + right) // 2

while left + 1 < right:
    mid = (left + right) // 2
    si = input_q(mid)
    if si == 0:
        left = mid
    else:
        right = mid

print("!", left, flush=True)