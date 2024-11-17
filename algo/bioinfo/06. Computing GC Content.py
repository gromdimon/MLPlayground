import operator

def read_fasta(fp):
    # Reading fasta format
    name = None
    seq = []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))  # interim genes
            name = line  # first name
            seq = []  # first seq
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))  # yields last gene

genes = {}  #  Reading fasta file
with open('test.txt') as fp:
    for name, seq in read_fasta(fp):
        genes[name] = seq


def counting_gc(genes):
    GC = {}
    for sample in genes:
        sample_length = len(genes[sample])
        GC_count = genes[sample].count('G') + genes[sample].count('C')  # Count G and C in sample
        percent = GC_count / sample_length
        GC[sample] = percent   # Appending GC frame
    return GC

GC = counting_gc(genes)
# Choosing string with highest GC content
sorted_GC = sorted(GC.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_GC[0])
