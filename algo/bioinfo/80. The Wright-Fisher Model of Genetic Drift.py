from scipy.special import comb

def gen_probability(n_individuals, copies_dominant, generations, copies_recessive):
    prob_recessive = 1 - copies_dominant / (2.0 * n_individuals)
    # probability of recessive allele in the 1 generation
    previous_p = [comb(2 * n_individuals, i) * prob_recessive ** i * (1 - prob_recessive) ** (2 * n_individuals - i) for i in range(1, 2 * n_individuals + 1)]

    # probabilities of given number of recessive alelles in generations 2, ..., g
    # P(1 Rec in current gen.) = P(1 Rec in current gen. | 0 rec in previous gen.) + ... +
    # P(1 rec in current gen. | 2N rec in previous gen.)
    for generation in range(2, generations + 1):
        current_p = []
        for j in range(1, 2 * n_individuals + 1):
            temp = [comb(2 * n_individuals, j) * (x / (2 * n_individuals)) ** j * (1 - x / (2 * n_individuals)) ** (2 * n_individuals - j) for x in range(1, 2 * n_individuals + 1)]
            current_p.append(sum(temp[i] * previous_p[i] for i in range(len(temp))))
        previous_p = current_p

    final_prob = sum(current_p[copies_recessive - 1:])
    return final_prob

N_individuals, m, g, k = [int(x) for x in input().split(' ')]
print(gen_probability(N_individuals, m, g, k))
