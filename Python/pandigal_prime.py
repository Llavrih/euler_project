import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_pandigital_set(n, b):
    digits = set(str(i) for i in range(1, b))
    num_digits = set(str(n))
    return digits == num_digits


for num in range(1, 999999999):
    if is_prime(num) is True:
        if is_pandigital_set(num, len(str(num)) + 1) is True:
            print(is_pandigital_set(num, len(str(num)) + 1), num)
