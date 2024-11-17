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

# Reading file
f = open('test.txt')
s = extract_sequence_from_input(f)

def reverse_seq(seq):
    library = {'A':'T',
               'C':'G',
               'T':'A',
               'G':'C'}
    new_seq= ''
    for nuckl in seq:  # For every nuckl choosing the opposite one
        new_seq += library[nuckl]
    return new_seq

list_of_normal = []
list_false = []
for seq in s:
    count = 0
    for r_seq in s:
        if seq == r_seq or seq == reverse_seq(seq) or seq == r_seq[::-1] or seq == reverse_seq(r_seq[::-1]):
            count += 1
    if count > 1 and seq not in list_of_normal:
        list_of_normal.append(seq)
    elif count < 2:
        list_false.append(seq)

def hamming_dist(string1, string2):
    return sum([x != y for x, y in zip(string1, string2)])

def ham_dist(seq, seq_cons):
    seq_cons_spis = []
    for s in seq_cons:
        seq_cons_spis.append(s)
        seq_cons_spis.append(reverse_seq(s[::-1]))
        seq_cons_spis.append(reverse_seq(s[::-1]))
        seq_cons_spis.append(s)
    for cons in seq_cons_spis:
        if hamming_dist(seq, cons) == 1:
            return cons

for f_seq in list_false:
    print(f_seq, '->', ham_dist(f_seq, list_of_normal), sep='')
