from math import factorial as fc

n, k = [int(x) for x in input().split(' ')]

ans = 0
for i in range(k, n + 1):  # All subsets
    ans += fc(n) // (fc(i) * fc(n - i))  # Math combinations

print(ans % int(1e6))
