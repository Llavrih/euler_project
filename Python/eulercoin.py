N = 1504170715041707
M = 4503599627370517
min_val = N
sum_val = N

def t_print(strings, lengths=[]):
    if len(lengths) < len(strings):
        lengths.extend(len(str(s)) for s in strings[len(lengths):])
    print("".join(str(strings[i]).ljust(lengths[i]) for i in range(len(strings))))

t_print(["Eulercoin", "Sum"], [20])
print("-"*36)
t_print([min_val, sum_val], [20])

Nn = N
while Nn > 100000000:
    Nn = (Nn + N) % M
    if Nn < min_val:
        min_val = Nn
        sum_val += Nn
        t_print([min_val, sum_val], [20])

t_print(["", "", "<< end brute-force attack"], [20, 18])
t_print(["", "", "<< start tail analysis"], [20, 18])

def modinv(a, n):
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return "a is not invertible"
    if t < 0:
        t += n
    return t

invN = modinv(N, M)
n = (min_val * invN) % M 
eulercoins = {}
for Nn in range(1, min_val):
    n1 = (Nn * invN) % M
    eulercoins[n1] = Nn

for n, Nn in sorted(eulercoins.items()):
    if Nn < min_val:
        min_val = Nn
        sum_val += Nn
        t_print([min_val, sum_val], [20])
        if Nn == 1:
            t_print([0, sum_val], [20])
            break

print("\nSolution: ", sum_val)
