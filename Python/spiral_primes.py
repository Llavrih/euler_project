import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def spiral():
    prime_count = 0
    total_diagonal_count = 1 
    side_length = 1
    current_number = 1
    
    while True:
        side_length += 2  
        for i in range(4):  
            current_number += side_length - 1
            if is_prime(current_number):
                prime_count += 1
        total_diagonal_count += 4  #
        
        prime_ratio = prime_count / total_diagonal_count
        if prime_ratio < 0.1:
            break
        
    return side_length

side_length = spiral()
print(f"Side length: {side_length}")
