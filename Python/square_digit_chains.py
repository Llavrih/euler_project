def square_digit_sum(n):
    return sum(int(digit)**2 for digit in str(n))

def ends_in_89(n):
    while n not in (1, 89):
        n = square_digit_sum(n)
    return n == 89

def count_numbers_ending_in_89(limit):
    count = 0
    for start in range(1, limit):
        if ends_in_89(start):
            count += 1
    return count

limit = 10000000  
print(count_numbers_ending_in_89(limit))
