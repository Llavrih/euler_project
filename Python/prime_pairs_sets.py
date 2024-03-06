from itertools import combinations
import math

def sieve(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n) if prime[p]]

def is_prime(n, primes):
    return n in primes

def all_prime_concatenations(prime_list, primes_set):
    for p1, p2 in combinations(prime_list, 2):
        if int(str(p1) + str(p2)) not in primes_set or int(str(p2) + str(p1)) not in primes_set:
            return False
    return True

def find_prime_set(primes, primes_set, set_size=5):
    for combination in combinations(primes, set_size):
        if all_prime_concatenations(combination, primes_set):
            return sum(combination)
    return None

limit = 100000  
primes = sieve(limit)
primes_set = set(primes)  

result = find_prime_set(primes, primes_set, 5)
if result:
    print(f"Result: {result}")
else:
    print("Fail.")
