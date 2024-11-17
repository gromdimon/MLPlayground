def mortal_fibonacci(n, m):
    # Counting offsprings in every generation
    rabbits = [0] * m  # Defining generations
    rabbits[0] = 1  # Everything starts with the first rabbit
    for i in range(n-1):  # Number of cycles
        newborns = sum(rabbits[1:])  # Counting how many rabbits appears in this generation
        rabbits = [newborns] + rabbits[:m-1]  # Leaving rabbits that remain alive
    return sum(rabbits)

# Reading file
n, m = [int(x) for x in input().split(' ')]
print(mortal_fibonacci(n, m))
