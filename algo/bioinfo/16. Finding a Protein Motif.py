import urllib.request
from re import finditer

def import_fasta(id):
    # Receiving data from UniProt database
    urllib.request.urlretrieve("http://www.uniprot.org/uniprot/" + id + ".fasta", "temp.fa")
    file = open("temp.fa")
    string = []
    for line in file:
        if not line.startswith(">"):
            string.append(line.rstrip())
    string = "".join(string)
    return string

def finding_pro_mot(ids):
    for id in ids:
        fasta_string = import_fasta(id)
        # Finding all positions in motif
        locations = [k.start() + 1 for k in finditer(r'(?=N[^P][ST][^P])', fasta_string)]  # finditer find a particular
        if len(locations) != 0:  # Printing only ids that have solutions                  position that matches criteria
            print(id)
            print(" ".join(map(str, locations)))

# Reading file
file = open('test.txt')
ids = file.read().splitlines()
finding_pro_mot(ids)


