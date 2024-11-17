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

file = open('test.txt')
seq = extract_sequence_from_input(file)
s1, s2 = seq[0], seq[1]
TI_DICT = {"A": "G", "G": "A", "C": "T", "T": "C"}

def ti_tv_ratio(string1, string2):
    num_ti = 0  # Number of transitions
    num_tv = 0  # Number of transversions

    for sym1, sym2 in zip(string1, string2):  # Going throw all symbols and choosing missmatchings
        if sym1 != sym2:
            if sym2 == TI_DICT[sym1]:
                num_ti += 1
            else:
                num_tv += 1

    return num_ti / num_tv

print(ti_tv_ratio(s1, s2))
