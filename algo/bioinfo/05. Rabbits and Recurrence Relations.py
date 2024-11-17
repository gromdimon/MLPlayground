def reccurence_relation(generations, offsprings_monthly):
    # Counting rabbits in given generation
    counter = 1
    new = 0  # Newborn rabbits
    old = 0  # Post-reproductive rabbits
    for _ in range(generations - 2):
        fertile = 1 + old  # Rabbits that give newborns
        offsprings = fertile * offsprings_monthly  # Newborn rabbits in this particular generation
        counter += offsprings  # Total number of rabbits
        old += new  # Rabbits, that gave birth in this generation, move to old category
        new = offsprings  # Offspring will be fertile rabbits in new generation
    return counter

# Reading file
generations, offsprings_monthly = int(input().split())
print(reccurence_relation(generations, offsprings_monthly))
