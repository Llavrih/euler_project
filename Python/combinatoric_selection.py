from math import comb

n_max = 100
threshold = 10**6

count = 0
for n in range(1, n_max + 1):
    for r in range(0, n + 1):
        if comb(n, r) > threshold:
            count += 1

print(count)