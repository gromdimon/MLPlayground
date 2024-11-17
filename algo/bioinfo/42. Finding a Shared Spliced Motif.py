# Open file feature
def extract_sequences(data):
    seq = []
    result = ''
    for line in data:
        if line.startswith('>'):
            seq.append(result)
            result = ''
        else:
            result += line[:-1]
    seq.remove('')
    seq.append(result)
    return seq


# Opening file
file = open('test.txt')
samples = extract_sequences(file)
samples_sorted = sorted(samples, key=len, reverse=False)
shortest = samples_sorted[0]
longest = samples_sorted[1]

def shared_spliced_motif(shortest, longest):
    lengths = [[0 for j in range(len(longest) + 1)] for i in range(len(shortest) + 1)]  # This builds matrix of 0
    # creates array of len(s) containing arrays of len(t) filled with 0
    for id_s, value_s in enumerate(shortest):
        for id_l, value_l in enumerate(longest):
            if value_s == value_l:  # If there is matching
                lengths[id_s + 1][id_l + 1] = lengths[id_s][id_l] + 1
            else:
                lengths[id_s + 1][id_l + 1] = max(lengths[id_s + 1][id_l], lengths[id_s][id_l + 1])  # Shift rights or downs
    spliced_motif = ''
    value_s, value_l = len(shortest), len(longest)
    while value_s * value_l != 0:  # Going from end to start, parallely finding motif
        if lengths[value_s][value_l] == lengths[value_s - 1][value_l]:  # If match shift lefts
            value_s -= 1
        elif lengths[value_s][value_l] == lengths[value_s][value_l - 1]:  # If match shifts ups
            value_l -= 1
        else:
            spliced_motif = shortest[value_s - 1] + spliced_motif  # If there is no matching shift cornerwise
            value_s -= 1
            value_l -= 1
    return spliced_motif

print(shared_spliced_motif(shortest, longest))
