def cycle_string(DNA):
    # Parsing edges from input
    edge_list = set()
    for string in DNA:
        edge_list.add(string)

    # Making prefix - suffix pares
    leng = len(DNA[0])
    edges = [[edg[0:leng - 1], edg[1:leng]] for edg in edge_list]

    # Go throw every seq and appending new symbols
    current = edges.pop(0)
    consensus = current[0][-1]
    while edges:
        consensus += current[1][-1]  # + last letter

        # Finding next seq pairs
        index = ''
        for id, value in enumerate(edges):
            if value[0] == current[1]:
                index = id
        current = edges.pop(int(index))

    return consensus

# Reading file
file = open('test.txt')
input_lines = file.read().splitlines()
# Applying function
result = cycle_string(input_lines)
print(result)
