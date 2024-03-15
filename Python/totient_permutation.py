import numpy as np

def optimized_calculate_phi(n):
    phi = np.arange(n + 1)
    for p in range(2, n + 1):
        if phi[p] == p:
            for multiple in range(p, n + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

n = 10_000_000
phi_values = optimized_calculate_phi(n)

min_ratio = float('inf')
min_n = 0
for i in range(2, n+1):
    if is_permutation(i, phi_values[i]):
        ratio = i / phi_values[i]
        if ratio < min_ratio:
            min_ratio = ratio
            min_n = i


print(min_n)
