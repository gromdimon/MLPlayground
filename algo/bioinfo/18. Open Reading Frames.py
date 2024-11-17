CODON_TBL = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}

def extract_sequences(data):
    # Reading fasta file
    seq = []
    result = ''
    for line in data:
        if line.startswith('>'):  # Start position
            seq.append(result)  # Appending last seq
            result = ''
        else:
            result += line[:-1]  # Forming result
    seq.remove('')
    seq.append(result)
    return seq

# Opening file
file = open('test.txt')
samples = extract_sequences(file)
s = samples[0]

def possible_proteins(string):
    start_pos_list = []
    for i in range(len(string) - 2):
        if string[i:i + 3] == "ATG":  # Start position of protein
            start_pos_list.append(i)  # Making list of start positions
    protein_list = set()
    for start_pos in start_pos_list:
        protein = ""
        for i in range(start_pos, len(string) - 2, 3):
            triplet = string[i:i + 3].replace("T", "U")  # Making RNA from DNA
            aa = CODON_TBL[triplet]  # Defining aminoacid
            if aa == "STOP":
                protein_list.add(protein)  # Appending protein if it has finish point (STOP)
                break
            protein += aa
    return protein_list

print(possible_proteins(s))
