def sex_inheritance(male):
    # The function, that counts probability of x is found among females
    female = male * (1 - male) * 2
    return female

# Reading file
A = [float(x) for x in input().split(' ')]
for a in A:
    print(sex_inheritance(a))
