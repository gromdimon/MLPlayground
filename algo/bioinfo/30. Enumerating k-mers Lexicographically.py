def permutation(alphabet, number, acc = '', res = []):
    # Cyclic function, that finds all possibles combinations of symbols
    if number == 0:  # If that was the last letter and you have final result
        res.append(acc)
    else:
        for letter in alphabet:  # For letters on next layer
            permutation(alphabet, number - 1, acc + letter, res)  # Finding all possibles combinations
    return res

# Reading file
letters = [i for i in input().split(' ')]
num = int(input())
sorted_permutations = permutation(letters, num)
print(sorted_permutations)
