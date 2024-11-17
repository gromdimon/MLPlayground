def expected_num_str(n, string, gc_cont):
    num_gc = string.count('G') + string.count('C')
    num_at = string.count('A') + string.count('T')
    num_slot = n - len(string) - 1
    # Counting probability, that modeled string with gc_content will match given string
    prob = ((gc_cont * 0.5) ** num_gc) * (((1 - gc_cont) * 0.5) ** num_at)
    return prob * num_slot

# Reading file
file = open('test.txt')
s = [s.rstrip() for s in file.readlines()]
n = int(s[0])
string = s[1]
gc = [float(x) for x in s[2].split(' ')]

for i in gc:
    print(expected_num_str(n, string, i), end=' ')
