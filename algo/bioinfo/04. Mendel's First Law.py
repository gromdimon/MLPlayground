def mendel_first_law(k, m, n):
    # Counting all the mates
    t = sum(map(float, [k, m, n]))  # (t-1) indicate that the first haplotype was select
    # Counting all ways of production an organism A_
    couples = [
        k * (k - 1),  # AA x AA
        k * m,  # AA x Aa
        k * n,  # AA x aa
        m * k,  # Aa x AA
        m * (m - 1) * 0.75,  # Aa x Aa
        m * n * 0.5,  # Aa x aa
        n * k,  # aa x AA
        n * m * 0.5,  # aa x Aa
        n * (n - 1) * 0  # aa x aa
    ]
    probability_of_A_ = sum(couples) / t / (t - 1)
    return probability_of_A_
# Extracting information from input
k, m, n = [float(x) for x in input().split(' ')]
print(mendel_first_law(k, m, n))
