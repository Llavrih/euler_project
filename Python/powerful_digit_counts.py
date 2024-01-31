def is_n_digit(num, n):
    if len(str(num)) == n:
        return True
    else:
        return False


i = 0
for n in range(1, 1000):
    for num in range(1, 10000):
        if is_n_digit(num**n, n) is True:
            i += 1
            print(i)
