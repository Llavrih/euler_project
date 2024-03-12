from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(limit):
    primes = []
    prime = [True for _ in range(limit + 1)]
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, limit):
        if prime[p]:
            primes.append(p)
    return primes

def generate_patterns(s):
    patterns = []
    for i in range(1, len(s)):  
        for combo in combinations(range(len(s)), i):
            pattern = list(s)
            for idx in combo:
                pattern[idx] = '*'
            patterns.append(''.join(pattern))
    return list(set(patterns))  

def find_smallest_prime_with_family(family_size):
    number = 1
    while True:
        number += 1
        if not is_prime(number):
            continue
        patterns = generate_patterns(str(number))
        for pattern in patterns:
            count = 0
            for digit in '0123456789':
                candidate = int(pattern.replace('*', digit))
                if pattern[0] != '*' and digit == '0': 
                    continue
                if candidate >= number and is_prime(candidate):
                    count += 1
            if count == family_size:
                return number

print(find_smallest_prime_with_family(8))
