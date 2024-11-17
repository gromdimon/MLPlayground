file = open('test.txt')
data = file.read().split('\n')

# Adding first string
first = data[0]
data = data[1:]
list_pos = []
list_values = []
n = 1
for lit in first:
  list_pos.append('{0} {1}'.format(n, n+1))
  list_values.append(lit)
  n += 1

def build_trie(data):
  current = len(list_values) + 2  # Position of node
  for root in data:  # Go throw data
    for index, val in enumerate(root):  # Every symbol
      for pos in list_pos:  # Comparing start positions
        start_end = pos.split(' ')
        start = int(start_end[0])
      if index + 1 == start or val == list_values[index]:  # Also comparing values of appropriate position
        pass
      else:
        list_pos.append('{0} {1}'.format(int(index) + 1, int(current)))  # Adding new edge
        current += 1
        list_values.append(val)

  return list_pos, list_values

positions, values = build_trie(data)
for i in range(len(positions)):
  print(positions[i], values[i])
