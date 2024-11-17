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

def spliced_motif(dna, substring):
    answer = [0]
    for i in range(len(substring)):
        for j in range(len(dna)):
            if substring[i] == dna[j] and j > answer[-1] - 1:  # If symbol of substr equal to next symbol of DNA
                answer.append(j + 1)
                break
    return answer

file = open('test.txt')
sample = extract_sequences(file)
dna = sample[0]
substring = sample[1]
answer = spliced_motif(dna, substring)

print(*answer[1:])
print('Length of motif:', len(substring), 'Length of answer:', len(answer), 'Length of answer is +1, because there is 0 in start position.')
