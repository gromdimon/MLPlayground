def completing_tree(lines):
    n = int(lines[0])  # Number of nodes
    existing_edges = len(input_lines) - 1
    additional_edges = n - 1  # Tree with n nodes has n - 1 edges
    return existing_edges - additional_edges  # Additional edges

file = open('test.txt')
input_lines = file.readlines()
print(completing_tree(input_lines))
