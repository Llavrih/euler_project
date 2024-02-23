import itertools

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

per = itertools.permutations(values, 10)
i = 0
for val in per:
    i += 1
    if i == 1000000:
        print(*val)
