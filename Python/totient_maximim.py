import numpy as np

def calculate_phi(n):
    phi = np.arange(n + 1)
    for p in range(2, n + 1):
        if phi[p] == p: 
            phi[p] -= 1
            for multiple in range(2*p, n + 1, p):
                phi[multiple] *= (1 - 1/p)
    return phi

n = 1_000_000
phi_values = calculate_phi(n)

max_ratio = 0
max_n = 0
for i in range(2, n+1):
    ratio = i / phi_values[i]
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = i

print(max_n, phi_values[max_n], max_ratio)
