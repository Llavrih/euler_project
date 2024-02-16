import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


max_prime_sum = 0
longest_sequence = 0


for start in range(2, 1000):
    sum = 0
    for i in range(start, 1000000):
        if is_prime(i):
            sum += i
            sequence_length = i - start
            if sum > 1000000:
                break
            if is_prime(sum) and sequence_length > longest_sequence:
                max_prime_sum = sum
                longest_sequence = sequence_length

print(max_prime_sum)
