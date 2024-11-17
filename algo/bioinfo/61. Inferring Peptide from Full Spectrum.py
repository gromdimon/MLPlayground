MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


def find_normal_weight(protein_weight, spis_weights):
    for weight in spis_weights:  # Search throw the weights in spis of all weights
        for aminoacid in MASS_TABLE:  # Search throw aminoacids
            if abs(MASS_TABLE[aminoacid] - (weight - protein_weight)) < 0.01:  # Trying to find aa, that would
                return aminoacid                                               # perfectly pass to sumarized peptide
    return 0

# Reading file
file = open('test.txt')
lines = file.readlines()
n = (len(lines) - 3) / 2  # The length of peptide
spis_weights = [float(x) for x in lines]
protein = ""
current = spis_weights[1]
remaining_weights = spis_weights[2:]

while len(protein) < n:
    aa = find_normal_weight(current, remaining_weights)  # For every position finding suitable aminoacid
    if aa == 0:
        break
    else:
        protein += aa
        current += MASS_TABLE[aa]
        remaining_weights = list(filter(lambda w: w - current > 0, remaining_weights))

print(protein)
