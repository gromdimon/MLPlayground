def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res

put = input()
n = int(input())
letters = [i for i in put.split(' ')]
mixed_sp = []
for i in range(1, n + 1):
    mixed_sp.append(alpha_combs(letters, i))

sp = mixed_sp[-1]

order = dict(zip(letters, range(len(letters))))   # Sorting strings in the order of the letters in the last word
sorted_sp = sorted(sp, key=lambda word: [order[c] for c in word])
for s in sorted_sp:
    print(s)
