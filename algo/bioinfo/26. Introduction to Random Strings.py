from math import log10

def prob_of_string(string, gc):
    # This function calculates probability of given string by summarizing probabilities of each nucleotide
    nuc_probs = {"G": log10(gc / 2), "C": log10(gc / 2), "A": log10((1 - gc) / 2), "T": log10((1 - gc) / 2)}
    log_probability = 0
    for nuc in string:
        log_probability += nuc_probs[nuc]
    return log_probability

# Reading file
with open('test.txt') as file:
    strings = file.readlines()
    lines = [line.rstrip() for line in strings]
    DNA_string = lines[0]
    GC_list = [float(x) for x in lines[1].split(" ")]

prob_list = []
for GC_content in GC_list:
    prob_list.append(prob_of_string(DNA_string, GC_content))
print(*prob_list)
