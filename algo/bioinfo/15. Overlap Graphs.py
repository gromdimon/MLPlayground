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

for id in genes:  # Go throw the first line
    for id2 in genes:  # Throw the second
        if genes[id][-3:] == genes[id2][:3] and id != id2:  # Comparison triplets of strings
            print(id[1:], id2[1:])
