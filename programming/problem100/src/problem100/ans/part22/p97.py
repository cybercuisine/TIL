import math
from functools import reduce

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def count_semi_common_multiples(N, M, A):
    A_prime = [a // 2 for a in A]
    
    overall_lcm = reduce(lcm, A_prime)
    
    for a in A_prime:
        if (overall_lcm // a) % 2 == 0:
            return 0
    
    count = M // overall_lcm
    return (count + 1) // 2

N, M = map(int, input().split())
A = list(map(int, input().split()))

print(count_semi_common_multiples(N, M, A))