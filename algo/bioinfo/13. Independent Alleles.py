from math import factorial as fc

def k_from_n(n, k):
    # This function returns number of possible
    # variants of combination k substances from n list
    return fc(n) / (fc(k) * fc(n-k))

def num_of_handy(n, p, r):
    # The function returns number of useful variants from all of them
    return k_from_n(n, r) * p ** r * (1-p) ** (n-r)  # p ** r and (1 - p) ** (n - r) are probabilities

def overall_prob(generation, prob, expected):
    all_org = 2 ** generation  # Counting all the offsprings
    # The function summarizes probabilities of all suitable offsprings
    return sum(num_of_handy(all_org, prob, i) for i in range(expected))

generation, expect = [int(x) for x in input().split(' ')]
print(1 - overall_prob(generation, 0.25, expect))
