from itertools import permutations


def satisfies_conditions(digits):
    if int("".join(digits[1:4])) % 2 != 0:
        return False
    if int("".join(digits[2:5])) % 3 != 0:
        return False
    if int("".join(digits[3:6])) % 5 != 0:
        return False
    if int("".join(digits[4:7])) % 7 != 0:
        return False
    if int("".join(digits[5:8])) % 11 != 0:
        return False
    if int("".join(digits[6:9])) % 13 != 0:
        return False
    if int("".join(digits[7:10])) % 17 != 0:
        return False
    return True


total_sum = 0
valid_numbers = []
for p in permutations("1234567890"):
    if satisfies_conditions(p):
        number = int("".join(p))
        valid_numbers.append(number)
        total_sum += number

print(total_sum, valid_numbers)
