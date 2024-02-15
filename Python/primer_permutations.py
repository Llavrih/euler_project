import math

results = []


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for A in range(1000, 9999):
    for D in range(1, 3333):
        B = A + D
        C = A + 2 * D
        if C > 9999:
            break

        if sorted(str(A)) == sorted(str(B)) == sorted(str(C)):
            if is_prime(A) and is_prime(B) and is_prime(C):
                results.append((A, B, C))
            break

print(results)
