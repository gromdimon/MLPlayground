def count_disease(A):
    B = []
    # Counting Aa and aa probability for every input number
    for a in A:
        B.append(a + 2 * a ** 0.5 * (1 - a ** 0.5))   # a ** 0.5 is frequency of a
    return B

# Reading file
A = [float(x) for x in input().split(' ')]
print(*count_disease(A))
