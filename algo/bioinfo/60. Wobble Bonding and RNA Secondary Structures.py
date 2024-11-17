f = open('test.txt')
strings = f.readlines()
string = ''
for s in strings:
    string += s[:-1]
f.close()

memo = {}
def wooble_count(seq):
    if len(seq) == 0 or len(seq) == 1:  # If there is only 1 way of connecting
        return 1

    if seq in memo:  # If there already is solution for sequence
        return memo[seq]

    memo[seq] = wooble_count(seq[1:])
    for i in range(4, len(seq)):
        if ((seq[0] == 'A' and seq[i] == 'U') or
                (seq[0] == 'U' and seq[i] == 'A') or
                (seq[0] == 'C' and seq[i] == 'G') or
                (seq[0] == 'G' and seq[i] == 'C') or
                (seq[0] == 'U' and seq[i] == 'G') or
                (seq[0] == 'G' and seq[i] == 'U')):
            memo[seq] += wooble_count(seq[1:i]) * wooble_count(seq[i+1:])  # All possible variance in two segments
    return memo[seq]

print(wooble_count(string))
