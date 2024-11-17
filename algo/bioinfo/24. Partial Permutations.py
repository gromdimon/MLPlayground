from math import factorial as fc

n, k = [int(x) for x in input().split(' ')]
part_perm = fc(n) / fc (n - k)  # Multiplying variants n * (n-1) * (n-2) ... * (n-k)
print(int(part_perm % 1e6))
