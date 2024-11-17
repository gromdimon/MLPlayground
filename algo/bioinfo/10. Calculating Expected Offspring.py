def calc_exp_offsprings(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa):
    # Counting dominant offsprings
    dominant_offspring = AAAA*2 + AAAa*2 + AAaa*2 + AaAa*1.5 + Aaaa
    return dominant_offspring

# Reading input
AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa = [int(i) for i in input().split(' ') ]
print(calc_exp_offsprings(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa))
