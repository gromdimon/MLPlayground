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

def finding_failure_array(dna):
    n = len(dna)
    symbol_mat = [0] * n

    for i in range(1, n):
        val = symbol_mat[i - 1]  #
        if val > 0 and dna[i] != dna[val]:  # If overlap ends
            val = symbol_mat[val - 1]
        if dna[i] == dna[val]:  # If there is match
            val += 1
        symbol_mat[i] = val
    return symbol_mat

file = open('test.txt')
seqs = extract_sequence_from_input(file)
seq = seqs[0]
failure_array = finding_failure_array(seq)
print(*failure_array)
