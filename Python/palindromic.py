def mirror(value):
    if isinstance(value, int):
        value = str(value)

    reversed_str = value[::-1]
    return reversed_str


def palindromic(a):
    return str(a) == mirror(a)


def decimalToBinary(n):
    return bin(n)[2:]


suma = 0
for i in range(1, 1000000):
    if palindromic(i) and palindromic(decimalToBinary(i)):
        print(i)
        suma += i
print(suma)
