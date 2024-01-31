def circulate_digits(number):
    str_num = str(number)
    length = len(str_num)
    rotations = [number]

    for i in range(1, length):
        str_num = str_num[-1] + str_num[:-1]
        rotations.append(int(str_num))

    return rotations


def is_prime_trial_division(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


count = 0
count_2 = 0
for i in range(1, 1000000):
    num = circulate_digits(i)
    if (is_prime_trial_division(i)) is True:
        for cd in num:
            if is_prime_trial_division(cd) is True:
                count_2 += 1
        if count_2 == len(num):
            count += 1
    count_2 = 0
print(count)
