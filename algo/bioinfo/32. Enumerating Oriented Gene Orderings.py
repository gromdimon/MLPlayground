from itertools import permutations

n = int(input())
perms = list(permutations(range(1, n + 1)))  # All possible permutations of string
print(perms)

def perm(n, permuts):
    for i in range(n):
        new_perm = []
        for perm in permuts:
            plus = perm
            minus = list(perm)
            minus[i] = -minus[i]  # Changing sign of one element
            new_perm += [minus, plus]
        permuts = new_perm  # Appending final list

    print(len(permuts))
    for perm in permuts:
        print(' '.join([str(x) for x in perm]))

perm(n, perms)
