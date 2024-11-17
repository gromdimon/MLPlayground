def string_probability(number, gc_content, seq):
    prob = 1
    for nuc in seq:
        # Counting probability of this string
        if nuc in "GC":
            prob *= gc_content * 0.5
        else:
            prob *= (1 - gc_content) * 0.5
    return 1 - (1 - prob) ** number  # 1 - probability, that unsuitable string will appear (1 - prob) ** n

with open('test.txt') as file:
    lines = file.readlines()
    liness = [line.rstrip() for line in lines]
n, x = [i for i in liness[0].split(' ')]
n = int(n)
x = float(x)
dna = liness[1]
answer = string_probability(n, x, dna)
print(answer)
