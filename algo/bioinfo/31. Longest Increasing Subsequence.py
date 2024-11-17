import sys
def calculate_increasing_subseq(sequence):
    L = [[sequence[0]]]  # List of sequence values (numbers)
    for i in range(1, len(sequence)):
        L.append([])
        for j in range(i):
            if (sequence[j] < sequence[i]) and (len(L[i]) < len(L[j]) + 1):  # If current number is bigger
                L[i] = L[j][:]                                               # than previous
        L[i].append(sequence[i])  # Adding final variant
    lis = []
    max_len = 0
    for l in L:  # Choosing the longest spis
        if len(l) > max_len:
            max_len = len(l)
            lis = l
    return lis

# Reading file
n = int(sys.stdin.readline())
permutation = list(map(int, sys.stdin.readline().rstrip().split()))
LIS = calculate_increasing_subseq(permutation)
LDS = calculate_increasing_subseq(permutation[::-1])[::-1]

print(" ".join(map(str, LIS)))
print(" ".join(map(str, LDS)))
