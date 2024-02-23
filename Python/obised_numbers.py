import numpy as np


def sum_of_divisors(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma


limit = (
    28123 
)

abundant_numbers = np.array([i for i in range(1, limit + 1) if sum_of_divisors(i) > i])

can_be_written_as_abundant = np.array([False] * (limit + 1))
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        sum_of_abundants = abundant_numbers[i] + abundant_numbers[j]
        if sum_of_abundants <= limit:
            can_be_written_as_abundant[sum_of_abundants] = True
        else:
            break

non_abundant_sums = np.array(
    [i for i, x in enumerate(can_be_written_as_abundant) if not x and i > 0]
)
result = np.sum(non_abundant_sums)

print(result)
