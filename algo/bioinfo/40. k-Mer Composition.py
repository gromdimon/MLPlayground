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
str = s[0]

def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)  # Adding variant
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)  # Choosing next symbol and saving variant in acc
    return res

def kmer_comp(string, k = 4):
    all_kmers = alpha_combs(["A", "C", "G", "T"], k, )  # All possible variations of 4 nuckls
    result = {}
    for kmer in all_kmers:
        result[kmer] = 0
    for i in range(len(string) - k + 1):  # How many times kmer meets in string
        kmer = string[i:i + k]
        result[kmer] += 1
    return result

ans = kmer_comp(str, 4).values()
print(*ans)
