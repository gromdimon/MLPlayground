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
print(samples)
def superstring(strings):
    A_point = len(strings[0])  # Defining last symbol of segment
    B_point = A_point // 2 + 1  # Defining first symbol of segment
    super_string = strings.pop(0)  # Choosing basic string
    while strings:
        for read in strings:  # Sorting throw all the rows
            for l in range(B_point, A_point):  # Checking all of the lengths
                if read[-l:] == super_string[:l]:  # If there is overlap at the beginning
                    super_string = read + super_string[l:]
                    strings.remove(read)
                    break
                elif read[:l] == super_string[-l:]:  # If there is overlap at the end
                    super_string = super_string + read[l:]
                    strings.remove(read)
                    break

    return super_string

answer = superstring(samples)
print(answer)
