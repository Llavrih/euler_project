import math

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

def is_reversible_prime_square(n):
    root_n = int(n**0.5)
    if n != root_n**2 or not is_prime(root_n): return False
    reversed_n = reverse_number(n)
    root_reversed_n = int(reversed_n**0.5)
    return reversed_n == root_reversed_n**2 and is_prime(root_reversed_n) and not is_palindrome(n)

reversible_prime_squares = []
n = 2

while len(reversible_prime_squares) < 50:
    square = n**2
    if is_reversible_prime_square(square):
        reversible_prime_squares.append(square)
        print(len(reversible_prime_squares))
    n += 1
    

sum_of_reversible_prime_squares = sum(reversible_prime_squares)
print(sum_of_reversible_prime_squares)

