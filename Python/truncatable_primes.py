def is_prime_trial_division(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_truncatable_prime(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime_trial_division(int(str_n[i:])) or not is_prime_trial_division(
            int(str_n[:i])
        ):
            return False
    return True


# Find all truncatable primes
truncatable_primes = []
for i in range(10, 1000000):  # Adjusted upper limit for practicality
    if is_prime_trial_division(i) and is_truncatable_prime(i):
        truncatable_primes.append(i)
        if len(truncatable_primes) == 11:  # We need only 11 such primes
            break

sum_of_truncatable_primes = sum(truncatable_primes)
truncatable_primes, sum_of_truncatable_primes
