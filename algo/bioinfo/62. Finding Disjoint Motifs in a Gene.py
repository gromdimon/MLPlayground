from numpy import zeros

def interwoven(str1, str2, target):
    if len(target) == 0:
        return True
    elif str1[0] == str2[0] == target[0]:
        return interwoven(str1[1:], str2, target[1:]) or interwoven(str1, str2[1:], target[1:])
    elif str1[0] == target[0]:
        return interwoven(str1[1:], str2, target[1:])
    elif str2[0] == target[0]:
        return interwoven(str1, str2[1:], target[1:])
    else:
        return False
file = open('test.txt')
input_lines = file.readlines()
target = input_lines[0].rstrip()
lines = [x.rstrip() for x in input_lines[1:]]

 # Initialize the zero matrix.
M = zeros((len(lines), len(lines)), dtype=int)

# Run through all combinations of dna strings.
for i in range(len(lines)):
    for j in range(len(lines)):
        if i <= j:
                # Count the combined number of each type of nucleotide in given dna strands.
            current_profile = [(lines[i] + lines[j]).count(nuc) for nuc in "ACGT"]
                # Compare the current profile to each substring of the same length in the superstring.
            for index in range(len(target) - len(lines[i]) - len(lines[j]) + 1):
                    # Having an identical profile is a necessary condition in order to be interweavable, but less computationally intensive.
                if current_profile == [target[index:index + len(lines[i]) + len(lines[j])].count(nuc)
                                        for nuc in "ACGT"]:
                        # Check the interweave if the profiles match, add an extra character outside the alphabet to avoid index out of range errors.
                    if interwoven(lines[i] + '$', lines[j] + '$',
                                    target[index:index + len(lines[i]) + len(lines[j])]):
                        M[i][j] = 1
                        break
            # The comparison are symmetric, so we've already done these computations.
        else:
            M[i][j] = M[j][i]

for s in M:
    print(*s)
