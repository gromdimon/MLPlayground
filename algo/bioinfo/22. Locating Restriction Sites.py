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

sample = genes[name]

def is_palindrome(string):
    # The function proves, that string is palindrome (123456 - 654321)
    mirror_str = ''
    for i in string:
        if i == 'A':
            mirror_str += 'T'
        elif i == 'T':
            mirror_str += 'A'
        elif i == 'G':
            mirror_str += 'C'
        elif i == 'C':
            mirror_str += 'G'

    for j in range(len(string)):
        if j < len(string):
            if not string[j] == mirror_str[len(string)-j - 1]:
                return False
        else:
            return False
    return True

for start in range(len(sample)):
    for palindrome_length in range(4,13,2):  # Going through the string and finding palindromes
        if start + palindrome_length <= len(sample) and is_palindrome(sample[start : start + palindrome_length]):
            print(start + 1, palindrome_length)
