n = int(input())
# Tree with n nodes has n-1 edges. When we have k internal nodes (have 3 degrees) and m rooted nodes (we have only one)
# and they have 2 degrees, number of leaves is k + m - 1
# An unrooted tree with n leaves and k internal nodes should have n + 3k total degrees.
# n + 3k = (n + k - 1) * 2
# m = n - 2
print(n - 2)
