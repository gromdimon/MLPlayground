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

# Reading file
file = open('test.txt')
lines = extract_sequence_from_input(file)
RNA = lines[0]
# Actually the answer is equal to the following expression
print(fc(RNA.count("A")) * fc(RNA.count("C")))
