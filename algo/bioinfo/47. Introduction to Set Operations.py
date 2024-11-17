n = int(input())
A = [int(x) for x in input()[1:-1].split(', ')]
B = [int(x) for x in input()[1:-1].split(', ')]
list_ab = []
for i in A:
    list_ab.append(i)
for i in B:
    if i not in list_ab:
        list_ab.append(i)
print(list_ab)
list_a_b = []
for lit in A:
    if lit in B:
        list_a_b.append(lit)
print(list_a_b)
list_a_b_ = []
for lit in A:
    if lit not in B:
        list_a_b_.append(lit)
print(list_a_b_)
list_b_a = []
for lit in B:
    if lit not in A:
        list_b_a.append(lit)
print(list_b_a)
list_a = []
for i in range(1, n + 1):
    if i not in A:
        list_a.append(i)
print(list_a)
list_b = []
for i in range(1, n + 1):
    if i not in B:
        list_b.append(i)
print(list_b)
