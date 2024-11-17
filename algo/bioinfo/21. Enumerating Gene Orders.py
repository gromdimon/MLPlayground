def permutation(spis):
    # If lst is empty then there are no permutations
    if len(spis) == 0:
        return []
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(spis) == 1:
        return [spis]
    perm = []
    for i in range(len(spis)):
        m = spis[i]
        # Deleting i from spis
        next_spis = spis[:i] + spis[i + 1:]
        # Finding next symbol
        for p in permutation(next_spis):
            perm.append([m] + p)
    return perm


# Reading file
data = [int(x) for x in range(1, int(input()) + 1)]
ans = permutation(data)
print(len(ans))
for x in ans:
    print(*x)
