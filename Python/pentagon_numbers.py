import math


def pentagonalNum(n):
    return (3 * n * n - n) // 2


def isPentagonal(N):
    n = (1 + math.sqrt(24 * N + 1)) / 6
    return (n - int(n)) == 0


min_D = None
pair = (0, 0)
limit = 3000
pentagonal_numbers_extended = [pentagonalNum(n) for n in range(1, limit + 1)]

for j in range(len(pentagonal_numbers_extended)):
    for k in range(j + 1, len(pentagonal_numbers_extended)):
        Pj = pentagonal_numbers_extended[j]
        Pk = pentagonal_numbers_extended[k]
        sumPkPj = Pj + Pk
        diffPkPj = abs(Pk - Pj)

        if isPentagonal(sumPkPj) and isPentagonal(diffPkPj):
            if min_D is None or diffPkPj < min_D:
                min_D = diffPkPj
                pair = (Pj, Pk)

print(min_D, pair)
