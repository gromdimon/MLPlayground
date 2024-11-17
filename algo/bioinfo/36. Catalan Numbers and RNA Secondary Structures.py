def extract_sequence_from_input(file):
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

memo = {}
def catalan(seq):
    if len(seq) == 0 or len(seq) == 1:  # If there is too short seq
        return 1
    total = 0
    if seq in memo:
        return memo[seq]

    for i in range(1, len(seq), 2):  # Finding all pairs in graph
        if ((seq[0] == 'A' and seq[i] == 'U') or
            (seq[0] == 'U' and seq[i] == 'A') or
            (seq[0] == 'C' and seq[i] == 'G') or
            (seq[0] == 'G' and seq[i] == 'C')):
            total += catalan(seq[1:i]) * catalan(seq[i + 1:])  # Summarizing variants in two spheres of graph
    # This equals to the formula of Catalan numbers
    memo[seq] = total % 10 ** 6  # Returning modulo answer
    return memo[seq]

# Reading file
f = open('test.txt')
s = extract_sequence_from_input(f)
string = s[0]
number = len(string)

print(catalan(string))
