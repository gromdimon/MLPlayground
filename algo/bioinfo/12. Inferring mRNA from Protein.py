reverse_table = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'G': 4,
    'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2,
    'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
    'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2
}

def inferring_rna(prot):
    possible = 1
    for aa in prot:
        possible *= reverse_table[aa]  # Multiplying possible variants by number of aa
    return possible * 3 % 1000000

# Reading file
protein = input()
print(inferring_rna(protein))
