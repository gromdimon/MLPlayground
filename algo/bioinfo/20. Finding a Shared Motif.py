def read_fasta(text):
    name = None
    seq = []
    for line in text:
        line = line.rstrip()
        if line.startswith('>'):   # Starts with name
            if name: yield (name, ''.join(seq))  # Returning past Sequence
            name = line   # Initilazing new Name
            seq = []    # Initializing new Sequence
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))   # Returning last Sequence

genes = {}  # Frame to collect sequences
with open('test.txt') as fasta_file:   # Open test file
    for name, seq in read_fasta(fasta_file):
        genes[name] = seq   # Appending genes with Name label and seq content

def is_substr(find, data):
    if len(find) < 1 and len(data) < 1:  # If we have no substr or data
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

def longest_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:  # If we have no data or sample is too short
        for start_letter in range(len(data[0])):   # Defining first nucleotide
            for lnth_substr in range(len(data[0]) - int(start_letter) + 1):   # And last one
                if lnth_substr > len(substr) and is_substr(data[0][start_letter:start_letter + lnth_substr], data):   # Condition - substring
                    substr = data[0][start_letter: start_letter + lnth_substr]
    return substr

strings = []
for names in genes:
    strings.append(genes[names])
print(longest_substr(strings))
