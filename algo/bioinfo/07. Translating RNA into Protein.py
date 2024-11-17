def rna_protein(rna):
    # Extracting codons from rna
    splitted_rna = []
    while rna:
        splitted_rna.append(rna[:3])
        rna = rna[3:]

    protein = ''  # Making protein string
    for codon in splitted_rna:
        if codon == 'AUG':
            protein += 'M'
        elif codon == 'GCC' or codon == 'GCG' or codon == 'GCU' or codon == 'GCA':
            protein += 'A'
        elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            protein += 'R'
        elif codon == 'CCC' or codon == 'CCU' or codon == 'CCA' or codon == 'CCG':
            protein += 'P'
        elif codon == 'ACC' or codon == 'ACU' or codon == 'ACA' or codon == 'ACG':
            protein += 'T'
        elif codon == 'GAA' or codon == 'GAG':
            protein += 'E'
        elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
            protein += 'I'
        elif codon == 'UUU' or codon == 'UUC':
            protein += 'F'
        elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
            protein += 'L'
        elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
            protein += 'S'
        elif codon == 'UAU' or codon == 'UAC':
            protein += 'Y'
        elif codon == 'UGU' or codon == 'UGC':
            protein += 'C'
        elif codon == 'UGG':
            protein += 'W'
        elif codon == 'CAU' or codon == 'CAC':
            protein += 'H'
        elif codon == 'CAA' or codon == 'CAG':
            protein += 'Q'
        elif codon == 'AAU' or codon == 'AAC':
            protein += 'N'
        elif codon == 'AAA' or codon == 'AAG':
            protein += 'K'
        elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
            protein += 'V'
        elif codon == 'GAU' or codon == 'GAC':
            protein += 'D'
        elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            protein += 'G'
        elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            break
    return protein

# Reading file
rna = input()
print(rna_protein(rna))
