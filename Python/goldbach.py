import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


composite = 9
i = 0
while composite - 2 * i**2 >= 2:
    if is_prime(composite - 2 * i**2):
        i = 0
        while True:
            composite += 2
            if not is_prime(composite):
                break
    else:
        i += 1

print(composite)
