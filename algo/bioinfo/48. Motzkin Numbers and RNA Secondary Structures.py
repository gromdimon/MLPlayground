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

f = open('test.txt')
s = extract_sequence_from_input(f)
string = s[0]

memo = {}
def motzkin(seq):
    if len(seq) == 0 or len(seq) == 1:  # If there is only 1 way of connecting
        return 1
    if seq in memo:  # If there already is solution for sequence
        return memo[seq]
    memo[seq] = motzkin(seq[1:])
    for i in range(1, len(seq)):
        if ((seq[0] == 'A' and seq[i] == 'U') or
                (seq[0] == 'U' and seq[i] == 'A') or
                (seq[0] == 'C' and seq[i] == 'G') or
                (seq[0] == 'G' and seq[i] == 'C')):
            memo[seq] += motzkin(seq[1:i]) * motzkin(seq[i + 1:])  # All possible variance in two segments
    return memo[seq]
print(motzkin(string))
