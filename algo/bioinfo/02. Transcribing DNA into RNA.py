def dna_rna(dna):
    # Replacing T with U
    string_RNA = ''
    for i in dna:
        if i == 'T':
            string_RNA += 'U'
        else:
            string_RNA += i
    return string_RNA

# Reading file
string_DNA = input()
print(dna_rna(string_DNA))
