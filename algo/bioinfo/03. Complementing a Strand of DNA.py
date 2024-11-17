def complementing_dna(dna):
    # Making complement string of dna
    complement = ''
    for i in range(len(string)):
        if string[i] == 'T':
            complement += 'A'
        elif string[i] == 'A':
            complement += 'T'
        elif string[i] == 'C':
            complement += 'G'
        elif string[i] == 'G':
            complement += 'C'
    return complement

# Reading file
string = input()
print(complementing_dna(string))
