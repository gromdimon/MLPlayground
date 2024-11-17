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

def hamm_dist(seq1, seq2):
    hamm = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:  # Counting missmatches
            hamm += 1
    return hamm

def distance_matrix(strings):
    n = len(strings[0])
    matrix = []
    for str1 in strings:
        current_hamm = []  # Each row in matrix
        for str2 in strings:
            current_hamm.append(hamm_dist(str1, str2) / n)
        matrix.append(current_hamm)
    return matrix

file = open('test.txt')
seqs = extract_sequence_from_input(file)
dist_mat = distance_matrix(seqs)
for line in dist_mat:
    print(*line)
