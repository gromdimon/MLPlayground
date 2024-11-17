def prot_mass(protein):
    mass = 0
    for amino in protein:  # Finding suitable protein and add its mass
        if amino == 'A':
            mass += 71.03711
        elif amino == 'C':
            mass += 103.00919
        elif amino == 'D':
            mass += 115.02694
        elif amino == 'E':
            mass += 129.04259
        elif amino == 'F':
            mass += 147.06841
        elif amino == 'G':
            mass += 57.02146
        elif amino == 'H':
            mass += 137.05891
        elif amino == 'I':
            mass += 113.08406
        elif amino == 'K':
            mass += 128.09496
        elif amino == 'L':
            mass += 113.08406
        elif amino == 'M':
            mass += 131.04049
        elif amino == 'N':
            mass += 114.04293
        elif amino == 'P':
            mass += 97.05276
        elif amino == 'Q':
            mass += 128.05858
        elif amino == 'R':
            mass += 156.10111
        elif amino == 'S':
            mass += 87.03203
        elif amino == 'T':
            mass += 101.04768
        elif amino == 'V':
            mass += 99.06841
        elif amino == 'W':
            mass += 186.07931
        elif amino == 'Y':
            mass += 163.06333

    return mass

# Reading file
protein = input()
print(prot_mass(protein))
