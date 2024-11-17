from math import factorial as fc

def extract_sequence_from_input(file):
    '''
    Reading fasta format
    :param fp: multiples string on different lines
    :return: sequences as list
    '''
    sequences = []
    result = ""
    for line in file:
        if ">" in line:
            sequences.append(result)  # Appending sequence list with final seq
            result = ""  # Initiation of a new seq
        else:
            if "\n" in line:
                result += line[:len(line) - 1]  # Lengthening of sequence
            else:
                result += line
    sequences.append(result)  # Appending list with last seq
    sequences.remove('')
    return sequences

def combinations(x, y):
    n = max(x, y)
    k = min(x, y)
    return fc(n) // fc(n-k)  # Math formula of all possible combinations

def max_match(string):
    A = string.count('A')
    C = string.count('C')
    G = string.count('G')
    U = string.count('U')
    return combinations(A, U) * combinations(C, G)  # Number of combinations of pairings A & U and G & C

file = open('test.txt')
strings = extract_sequence_from_input(file)
rna = strings[0]
answer = max_match(rna)
print(answer)
