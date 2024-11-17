def Newick(newick, pair):
    # Finding positions of organisms
    first = newick.find(pair[0])
    sekond = newick.find(pair[1])
    path = ''

    start = min(first, sekond)
    end = max(first, sekond) + 1

    for index in range(start, end):
        if newick[index] in ',()':
            path += newick[index]

    # Replacing all similar neighborhood symbols
    while ',,' in path: path = path.replace(',,', ',')
    while '(,)' in path: path = path.replace('(,)', '')

    dist = path.count('(') + path.count(')') + 2 * int(',' in path)

    return dist

file = open('test.txt')
lines = file.readlines()
file.close()

for i in range(0, len(lines), 3):
    nwck = lines[i][:-1]
    organisms = lines[i + 1][:-1].split(' ')
    print(Newick(nwck, organisms), end=' ')
