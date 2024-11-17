def reverse_comp(dnaStrand):
    """This function gets the reverse complement of the strand"""
    complement_DNA = ""
    dnaSequence = list(dnaStrand)
    dnaSequence.reverse()
    dnaStrand = ''.join(dnaSequence)
    complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}
    for base in dnaStrand:
        complement_DNA += complementDict[base]

    return complement_DNA


def de_bruijn(dna_semples):
    dna_dict = set()
    for sampl in dna_semples:
        dna_dict.add(sampl)
        dna_dict.add(reverse_comp(sampl))
    ans_list = []
    for seq in dna_dict:
        ans_list.append((seq[:len(seq)-1], seq[1:]))
    return ans_list

file = open('test.txt')
line = file.readlines()
lines = [line.rstrip() for line in line]
file.close()

ans = de_bruijn(lines)
for i in ans:
    print("(" + i[0] + ", " + i[1] + ")")
