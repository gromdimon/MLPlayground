def point_mutations(seq1, seq2):
    # The function goes through every symbol of strings and counts discrepancies
    counter_mutations = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            counter_mutations += 1
    return counter_mutations

# Reading file
seq1, seq2 = input(), input()
print(point_mutations(seq1, seq2))
