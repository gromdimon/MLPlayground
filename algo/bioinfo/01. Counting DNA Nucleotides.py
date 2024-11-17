def count_symbols(string):
    # The function counts different symbols in string
    counts_list = []
    counts_list.append(string.count('A'))
    counts_list.append(string.count('C'))
    counts_list.append(string.count('G'))
    counts_list.append(string.count('T'))
    return counts_list

# Reading file
file = open('test.txt')
line = ''
lines = [x.rstrip() for x in file.readlines()]
for l in lines:
    line += l
print(count_symbols(line))
