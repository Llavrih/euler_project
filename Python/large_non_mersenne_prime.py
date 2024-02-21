base = 28433
exponent = 7830457
modulus = 10**10

last_ten_digits = (base * pow(2, exponent, modulus) + 1) % modulus

print(last_ten_digits)