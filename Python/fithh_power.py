n = 1
while 10 ** (n - 1) <= n * 9**5:
    n += 1
upper_limit = 10**n  # Upper limit for the search

# Finding all numbers that can be written as the sum of the fifth powers of their digits
sum_of_numbers = 0
for i in range(
    10, upper_limit
):  # Starting from 10 as single digit numbers are not considered
    if i == sum(int(digit) ** 5 for digit in str(i)):
        sum_of_numbers += i

sum_of_numbers
