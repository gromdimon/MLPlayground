from math import factorial as fc
from math import log10

def prob(n, k, p = 0.5):
    # The function counts probability, that two people have k common substances from n (all substances)
    variants = fc(n) // (fc(k) * fc(n - k))
    prob_event = p ** k * (1 - p) ** (n - k)
    return variants * prob_event

n = int(input())
for k in range(1, 2 * n + 1):
    cum_pr = sum(prob(2 * n, i) for i in range(k, 2 * n + 1)) # Counting also variants with more than k substances
    print(log10(cum_pr), end=' ')
